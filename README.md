# Flask CRUD API with MongoDB

This project is a simple Flask-based REST API that demonstrates basic CRUD (Create, Read, Update, Delete) operations using **MongoDB** as the backend database.

---

## Features

- REST API built with **Flask**
- Supports **GET, POST, PUT, DELETE** HTTP methods
- Stores and retrieves data from **MongoDB** using `pymongo`
- Single endpoint (`/sample`) handling multiple operations

---

## Tech Stack

- Python 3
- Flask
- MongoDB
- PyMongo

---

## API Endpoint

### `/sample`

Supports the following HTTP methods:

#### 1. **GET**
Fetch all records from the database.

**Response Example**
```json
{
  "success": true,
  "data": [
    {
      "name": "John",
      "address": "Mumbai"
    }
  ]
}
