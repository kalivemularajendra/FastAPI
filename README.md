# FastAPI Project

This repository contains two simple FastAPI applications: a **Student Course API** and a **Todo List API**.

---

## 🌟 Student Course API

A sample application showcasing how to use FastAPI to add a ReST API to a MongoDB collection.

### Features

* **Create, Read, Update, and Delete (CRUD)** operations for student records.
* Data validation using **Pydantic** models.
* Asynchronous MongoDB integration with **motor** and **pymongo**.

### Getting Started

#### Prerequisites

* Python 3.7+
* MongoDB

#### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/rajendrakanna/fastapi.git](https://github.com/rajendrakanna/fastapi.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd fastapi
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the application

1.  Set up your MongoDB connection string as an environment variable. Replace `<your_mongodb_connection_string>` with your actual connection string.
    ```bash
    export MONGODB_URL="<your_mongodb_connection_string>"
    ```
2.  Run the application using uvicorn:
    ```bash
    uvicorn fast:app --reload
    ```
3. You can now access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### API Endpoints

The following endpoints are available for the Student Course API:

* `POST /students/`: Add a new student record.
* `GET /students/`: List all student records.
* `GET /students/{id}`: Get a single student record by its unique ID.
* `PUT /students/{id}`: Update an existing student's information.
* `DELETE /students/{id}`: Delete a student record.

---

## ✅ Todo List API

A simple API for managing a to-do list. This application uses an in-memory list, so no database is required.

### Features

* **CRUD operations** for to-do items.
* **Priority levels** for to-dos (High, Medium, Low) using Python's `Enum`.
* In-memory data storage.

### Running the application

1.  Run the application using uvicorn:
    ```bash
    uvicorn todo:app --reload
    ```
2. You can now access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### API Endpoints

The following endpoints are available for the Todo List API:

* `POST /todos`: Create a new to-do item.
* `GET /todos`: Get all to-do items, with an optional `first_n` query parameter to limit results.
* `GET /todos/{todo_id}`: Get a single to-do item by its ID.
* `PUT /todos/{todo_id}`: Update an existing to-do item.
* `DELETE /todos/{todo_id}`: Delete a to-do item.

---

## 🚀 Technologies Used

* **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **Pydantic**: Data validation and settings management using Python type annotations.
* **MongoDB**: A NoSQL document-oriented database used for the Student Course API.
* **Motor**: The official asynchronous Python driver for MongoDB.
* **Uvicorn**: An ASGI server for running FastAPI applications.

