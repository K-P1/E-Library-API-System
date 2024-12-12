import logging
from schemas.book_schemas import WriteBook, ReadBook, UpdateBook, books
from fastapi import HTTPException
from services.fake_data import generate_id
from schemas.record_schemas import ReadBorrowRecord, UpdateBorrowRecord, WriteBorrowRecord, records
from schemas.user_schemas import users

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CRUDOperations")

class BookCrud:
    @staticmethod
    def create_book(book_data: WriteBook):
        try:
            logger.info("Attempting to create a new book entry.")
            book_id = generate_id("book")
            book = ReadBook(id=book_id, **book_data.model_dump())
            books[book_id] = book
            logger.info(f"Book created successfully with ID: {book_id}")
            return book
        except Exception as e:
            logger.error(f"Error creating book: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_book(book_id: str):
        logger.info(f"Fetching book with ID: {book_id}")
        book = books.get(book_id)
        if not book:
            logger.warning(f"Book with ID {book_id} not found.")
            raise HTTPException(status_code=404, detail="Book not found")
        logger.info(f"Book with ID {book_id} found.")
        return book

    @staticmethod
    def get_all_books():
        logger.info("Fetching all books.")
        return list(books.values())

    @staticmethod
    def update_book(book_id: str, book_data: UpdateBook):
        logger.info(f"Attempting to update book with ID: {book_id}")
        book = books.get(book_id)
        if not book:
            logger.warning(f"Book with ID {book_id} not found.")
            raise HTTPException(status_code=404, detail="Book not found")
        try:
            for key, value in book_data.model_dump(exclude_unset=True).items():
                setattr(book, key, value)
            books[book_id] = book
            logger.info(f"Book with ID {book_id} updated successfully.")
            return book
        except Exception as e:
            logger.error(f"Error updating book with ID {book_id}: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def change_book_availability(book_id: str):
        logger.info(f"Changing availability of book with ID: {book_id}")
        book = books.get(book_id)
        if not book:
            logger.warning(f"Book with ID {book_id} not found.")
            raise HTTPException(status_code=404, detail="Book not found")
        book.is_available = not book.is_available
        logger.info(f"Book availability {book.is_available} toggled for ID: {book_id}")
        return book

    @staticmethod
    def delete_book(book_id: str):
        logger.info(f"Attempting to delete book with ID: {book_id}")
        book = books.pop(book_id, None)
        if not book:
            logger.warning(f"Book with ID {book_id} not found.")
            raise HTTPException(status_code=404, detail="Book not found")
        logger.info(f"Book with ID {book_id} deleted successfully.")
        return book

    @staticmethod
    def borrow_book(data: WriteBorrowRecord):
        logger.info("Creating borrow record.")
        new_id = generate_id('record')
        user = users.get(data.user_id)
        book = books.get(data.book_id)
        if not user or not book:
            logger.warning("User or Book not found during borrow operation.")
            raise HTTPException(status_code=404, detail="User or Book not found")
        if book.is_available == False and user.is_active == False:
            logger.warning("Book is currently not available for borrowing and User is currently not active.")
            raise HTTPException(status_code=400, detail="Book is currently not available and User is currently not active")
        if not book.is_available:
            logger.warning("Book is currently not available for borrowing.")
            raise HTTPException(status_code=400, detail="Book is currently not available")
        if not user.is_active:
            logger.warning("User is currently not active.")
            raise HTTPException(status_code=403, detail="User is currently not active")
        record = ReadBorrowRecord(
            id=new_id, 
            user_id=data.user_id, 
            book_id=data.book_id, 
            borrowed_at=data.borrowed_at,
            returned_at=None)
        records[new_id] = record
        book.is_available = False
        logger.info(f"Borrow record created with ID: {new_id}")
        return record

    @staticmethod
    def return_book(record_id: str, update_data: UpdateBorrowRecord):
        logger.info(f"Processing return for record ID: {record_id}")
        record = records.get(record_id)
        if not record:
            logger.warning(f"Record with ID {record_id} not found.")
            raise HTTPException(status_code=404, detail="Record not found")
        if update_data.returned_at:
            record.returned_at = update_data.returned_at
        records[record_id] = record
        book = books.get(record.book_id)
        book.is_available = True
        logger.info(f"Book returned and record updated for ID: {record_id}")
        return record

book_crud = BookCrud()