"""
Testing API methods in Python Flask
"""
# build in packages
from flask import Flask, request
import pymongo
app = Flask(__name__)
@app.route("/sample", methods=['POST', 'PUT', 'GET', 'DELETE'])
def function_get():
    """to generaget and store comments

    Returns:
        string: _description_
    """
    response = {}
    # to fetch input arguements from URL
    #input_args = request.args.to_dict()
    # data contains Body - Input JSON
    data = request.get_json()
    if request.method in ['PUT',"DELETE"]:
        # update memeber value basis user id
        update_member_value(data['id'], request.method)
        response['success'] = True
        response['status_text'] = "record updated successfully"
    if request.method == 'GET':
        list_objects = call_get_method()
        if list_objects:
            response['success'] = True
            response['data'] = list_objects
        else:
            response['success'] = False
            response['data'] = []
    if request.method == 'POST':
        flag = add_new_entry(data)
        if flag:
            response['success'] = True
            response['status_text'] = "new record added successfully"
        else:
            response['success'] = False
            response['status_text'] = "Error in adding new record entry"        
    return response

def update_member_value(user_id, request_method):
    """_summary_

    Args:
        user_id (int): _description_
    """    
    client = pymongo.MongoClient(local_host_string, port_number)
    database_name = client[database_name]    
    if request_method == 'PUT':
        for i in user_id:
            query_update = {"id": str(i)}
            update_value = {
                        "$set": {
                            "memeber": False
                        }
                    }
            database_name.test01.update_one(filter=query_update, update = update_value)
    elif request_method == 'DELETE':
        try:
            for i in user_id:
                query_update = {"id": str(i)}
                database_name.test01.delete_one(query_update)
        except Exception as ex:
            print(ex)

def call_get_method():
    """_summary_

    Returns:
        _type_: _description_
    """
    list_objects = []
    client = pymongo.MongoClient(local_host_string, port_number)
    database_name= client[database_name]
    cur_data = database_name.test01.find()
    for i in cur_data:
        list_objects.append({
                                "name": i['name'],
                                "address": i['address']
                            })
    return list_objects

def add_new_entry(input_data):
    """_summary_

    Args:
        input_data (dict): _description_

    Returns:
        _type_: _description_
    """

    flag = False
    client = pymongo.MongoClient(local_host_string, port_number)
    database_name= client[database_name]
    try:
        database_name.test01.insert_one(
            {
                "id" : input_data['id'],
                "name" : input_data['name'],
                "address" : input_data['address'],
                "age" : input_data["age"],
                "memeber" : input_data['memeber']
            }
        )
        flag = True
    except TypeError:
        flag = False
    return flag

app.run(port=5000, debug=True)