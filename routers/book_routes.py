from fastapi import APIRouter
from crud.book_crud import book_crud
from schemas.book_schemas import UpdateBook, WriteBook
from schemas.record_schemas import UpdateBorrowRecord, WriteBorrowRecord

books_router = APIRouter()

@books_router.post("/create", status_code=201)
async def create_book_endpoint(book_data: WriteBook):
    return book_crud.create_book(book_data)

@books_router.get("/get/{book_id}", status_code=200)
async def get_book_endpoint(book_id: str):
    return book_crud.get_book(book_id)

@books_router.get("/get_all/books", status_code=200)
async def get_all_books_endpoint():
    return book_crud.get_all_books()

@books_router.patch("/update/partial/{book_id}", status_code=200)
async def partial_update_book_endpoint(book_id: str, book_data: UpdateBook):
    return book_crud.update_book(book_id, book_data)

@books_router.put("/update/full/{book_id}", status_code=200)
async def full_update_book_endpoint(book_id: str, book_data: UpdateBook):
    return book_crud.update_book(book_id, book_data)

@books_router.patch("/change_availability/{book_id}", status_code=200)
async def change_book_availability_endpoint(book_id: str):
    return book_crud.change_book_availability(book_id)

@books_router.delete("/delete/{book_id}", status_code=200)
async def delete_book_endpoint(book_id: str):
    return book_crud.delete_book(book_id)

@books_router.post("/borrow", status_code=201)
async def borrow_book_endpoint(data: WriteBorrowRecord):
    record = book_crud.borrow_book(data)
    return record

@books_router.patch("/return/{record_id}", status_code=200)
async def return_book_endpoint(
    record_id: str, 
    returned_at: UpdateBorrowRecord):
    update_data = book_crud.return_book(record_id, returned_at)
    return update_data