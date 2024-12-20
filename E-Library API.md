# Project Title:  
**E-Library API System**  

## Description  
This project aims to develop a simple API for managing an online library system. The system enables users to borrow and return books, manage user profiles, and monitor book availability.

---

## System Entities  

### 1. User  
- **id**: Unique identifier for the user.  
- **name**: Name of the user.  
- **email**: Email address of the user.  
- **is_active**: Indicates whether the user account is active (default: `True`).  

### 2. Book  
- **id**: Unique identifier for the book.  
- **title**: Title of the book.  
- **author**: Author of the book.  
- **is_available**: Indicates whether the book is available for borrowing (default: `True`).  

### 3. BorrowRecord  
- **id**: Unique identifier for the borrowing record.  
- **user_id**: ID of the user who borrowed the book.  
- **book_id**: ID of the borrowed book.  
- **borrow_date**: Date the book was borrowed.  
- **return_date**: Date the book was returned (if applicable).  

---

## Requirements  

### 1. API Endpoints  

#### User Endpoints  
- CRUD operations for users.  
- Endpoint to deactivate a user by setting `is_active` to `False`.  

#### Book Endpoints  
- CRUD operations for books.  
- Endpoint to mark a book as unavailable (e.g., lost or under maintenance).  

#### Borrow Operations  
- **Borrow a Book**:  
  - Allows an active user to borrow an available book.  
  - Restricts borrowing if the book is unavailable or already borrowed by the user.  
  - If successful, sets the book’s `is_available` status to `False`.  
  - Returns an appropriate response and status code if unsuccessful.  
- **Return a Book**:  
  - Updates the `return_date` in the `BorrowRecord`.  
  - Resets the book’s `is_available` status to `True`.  

#### Borrow Record Management  
- Endpoint to retrieve borrowing records for a specific user.  
- Endpoint to view all borrowing records.  

---

## Additional Requirements  

### 1. Database  
- Use in-memory data structures (`list` or `dict`) for data storage.  

### 2. Validation  
- Implement Pydantic models for input validation across endpoints.  

### 3. Code Structure  
- Maintain a modular file structure for readability and scalability.  
- Separate files for models, routes, and application configuration.  

### 4. Status Codes  
- Ensure appropriate HTTP status codes for all success and error responses.  

---

## Constraints  
- Only active users can perform operations.  
- Books must be available to be borrowed.  
- Each borrowing operation must generate a unique `BorrowRecord`.  

---

## Submission Instructions  

- Use FastAPI to develop the project.  
- Include a `README.md` file with instructions for running the application.  
- Push the project to a public GitHub repository.  
- Add optional test cases for API endpoint validation to earn extra credit.  

### Submission Link  
[Submit your project here](https://forms.gle/7vpvT2qUAUrivvuU9)
