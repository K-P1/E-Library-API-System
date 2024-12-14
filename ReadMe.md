# E-Library API

The E-Library API is a backend system for managing an online library. It provides a way to create, retrieve, update, and delete users, books, and borrowing records, while maintaining an in-memory database for all operations.

## Features

- **User Management**:
  - Create, retrieve, update, and delete user profiles.
  - Track user activity status.

- **Book Management**:
  - Add, update, and delete book records.
  - Manage availability of books for borrowing.

- **Borrowing Records**:
  - Record borrowing and returning of books.
  - View borrowing history for specific users and specific books.

## Prerequisites

- Python 3.9 or higher.
- FastAPI framework.
- Uvicorn ASGI server.

## Installation

### Clone the Repository

```bash
git clone https://github.com/K-P1/E-Library-API-System.git
cd E-Library-API-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Server

Run the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be accessible at `http://127.0.0.1:8000`.

### API Documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Directory Structure

```plaintext
project/
├── crud/             # CRUD logic for users, books, and records
├── routers/          # API route definitions
├── schemas/          # Pydantic models for validation
├── services/         # Utility services like fake data generation
├── tests/            # Automated test cases
├── main.py           # Entry point for the application
├── README.md         # Documentation for the project
├── E-Library API.md  # Project plan and requirements
├── requirements.txt  # Python dependencies
```

## Usage

### User Endpoints

- **Create User**:
  - Endpoint: `POST /user/create`
  - Request Body:
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com",
        "is_active": true
    }
    ```

- **Get User**:
  - Endpoint: `GET /user/{user_id}`

- **Get All Users**:
  - Endpoint: `GET /user/get/all`

- **Update User (Partial)**:
  - Endpoint: `PATCH /user/update/partial/{user_id}`
  - Request Body:
    ```json
    {
        "name": "Updated Name"
    }
    ```

- **Update User (Full)**:
  - Endpoint: `PUT /user/update/full/{user_id}`
  - Request Body:
    ```json
    {
        "name": "Updated Name",
        "email": "updated@example.com",
        "is_active": false
    }
    ```

- **Deactivate User**:
  - Endpoint: `PATCH /user/deactivate/{user_id}`

- **Delete User**:
  - Endpoint: `DELETE /user/delete/{user_id}`

### Book Endpoints

- **Create Book**:
  - Endpoint: `POST /book/create`
  - Request Body:
    ```json
    {
        "title": "Book Title",
        "author": "Author Name",
        "is_available": true
    }
    ```

- **Get Book**:
  - Endpoint: `GET /book/get/{book_id}`

- **Get All Books**:
  - Endpoint: `GET /book/get_all/books`

- **Update Book (Partial)**:
  - Endpoint: `PATCH /book/update/partial/{book_id}`
  - Request Body:
    ```json
    {
        "title": "New Title"
    }
    ```

- **Update Book (Full)**:
  - Endpoint: `PUT /book/update/full/{book_id}`
  - Request Body:
    ```json
    {
        "title": "Updated Title",
        "author": "Updated Author",
        "is_available": false
    }
    ```

- **Change Availability**:
  - Endpoint: `PATCH /book/change_availability/{book_id}`

- **Delete Book**:
  - Endpoint: `DELETE /book/delete/{book_id}`

- **Borrow Book**:
  - Endpoint: `POST /book/borrow`
  - Request Body:
    ```json
    {
        "user_id": "us_1234",
        "book_id": "bk_5678"
    }
    ```

- **Return Book**:
  - Endpoint: `PATCH /book/return/{record_id}`
  - Request Body:
    ```json
    {
        "returned_at": "2023-12-01"
    }
    ```

### Record Endpoints

- **Get All Records**:
  - Endpoint: `GET /record/get/all`

- **Get Records by User**:
  - Endpoint: `GET /record/get/user/{user_id}`

- **Get Records by Book**:
  - Endpoint: `GET /record/get/book/{book_id}`

- **Get Record by ID**:
  - Endpoint: `GET /record/get/{record_id}`

## Prefilled Fake Data

To facilitate testing and demonstration, the database is prefilled with fake data using the `Faker` library. This includes:

- **Users**: 10 randomly generated user profiles with unique IDs, names, and emails.
- **Books**: 20 book entries with unique titles, authors, and availability statuses.
- **Borrowing Records**: 50 borrowing records linking users and books, tracking borrow dates.

The fake data is generated through the `generate_initial_data` function in the `fake_data.py` file, ensuring realistic and varied entries for testing. 

## Running Tests

The project includes a suite of automated tests to validate the functionality of all endpoints. These tests ensure:

- **User Operations**: Validation of user creation, retrieval, updates (partial and full), activation, deactivation, and deletion.
- **Book Operations**: Ensuring books can be added, retrieved, updated, borrowed, returned, and deleted accurately.
- **Record Operations**: Verification of borrowing and returning functionality, as well as retrieval of records by user, book, or ID.

Tests are implemented in `test_main.py` and use `TestClient` from FastAPI for HTTP request simulations.

### Running the Tests

To execute the test suite, run the following command:

```bash
pytest
```

### Sample Output

A successful test run will display output similar to:

```plaintext
========================= test session starts ==========================
collected 30 items

 test_main.py .............................................. [100%]

========================= 30 passed in 2.34s ===========================
```

This ensures that all endpoints are functioning as expected and that the application is ready for production or further development.