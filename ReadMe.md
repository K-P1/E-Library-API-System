# README.md

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
  - View borrowing history for specific users.

## Prerequisites

- Python 3.9 or higher.
- FastAPI framework.
- Uvicorn ASGI server.

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-repo/elibrary-api.git
cd elibrary-api
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
  - Endpoint: `GET /user/get/{user_id}`

- **Update User**:
  - Endpoint: `PATCH /user/update/{user_id}`
  - Request Body:
    ```json
    {
        "name": "Updated Name"
    }
    ```

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

- **Update Book**:
  - Endpoint: `PATCH /book/update/{book_id}`
  - Request Body:
    ```json
    {
        "title": "New Title"
    }
    ```

- **Delete Book**:
  - Endpoint: `DELETE /book/delete/{book_id}`

### Borrowing Record Endpoints

- **Create Record**:
  - Endpoint: `POST /record/create`
  - Request Body:
    ```json
    {
        "user_id": "us_1234",
        "book_id": "bk_5678"
    }
    ```

- **Get Record**:
  - Endpoint: `GET /record/get/{record_id}`

- **Update Record**:
  - Endpoint: `PATCH /record/update/{record_id}`
  - Request Body:
    ```json
    {
        "returned_at": "2023-12-01"
    }
    ```

## Running Tests

To ensure all functionality works as expected, run the automated test suite:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Enjoy building your E-Library API!**
