from schemas.book_schemas import WriteBook, ReadBook, UpdateBook, books
from fastapi import HTTPException

class BookCrud:
    @staticmethod
    def create_book(book_data: WriteBook):
        book_id = f"bk_{len(books) + 1:04}"
        book = ReadBook(id=book_id, **book_data.dict())
        books[book_id] = book
        return book

    @staticmethod
    def get_book(book_id: str):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @staticmethod
    def get_all_books():
        return list(books.values())

    @staticmethod
    def update_book(book_id: str, book_data: UpdateBook):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(book, key, value)
        books[book_id] = book
        return book

    @staticmethod
    def delete_book(book_id: str):
        book = books.pop(book_id, None)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

book_crud = BookCrud()