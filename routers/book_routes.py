from fastapi import APIRouter, HTTPException
from crud.book_crud import book_crud
from schemas.book_schemas import UpdateBook, WriteBook

books_router = APIRouter()

@books_router.post("/create", status_code=201)
async def create_book_endpoint(book_data: WriteBook):
    return book_crud.create_book(book_data)

@books_router.get("/get/{book_id}", status_code=200)
async def get_book_endpoint(book_id: str):
    return book_crud.get_book(book_id)

@books_router.get("/get/all", status_code=200)
async def get_all_books_endpoint():
    return book_crud.get_all_books()

@books_router.patch("/update/{book_id}", status_code=200)
async def update_book_endpoint(book_id: str, book_data: UpdateBook):
    return book_crud.update_book(book_id, book_data)

@books_router.delete("/delete/{book_id}", status_code=200)
async def delete_book_endpoint(book_id: str):
    return book_crud.delete_book(book_id)