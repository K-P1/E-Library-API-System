from fastapi import APIRouter
from crud.record_crud import record_crud

records_router = APIRouter()

@records_router.get("/get/all", status_code=200)
async def get_all_records_endpoint():
    return record_crud.get_all_records()

@records_router.get("/get/user/{user_id}", status_code=200)
async def get_user_record_endpoint(user_id: str):
    return record_crud.get_user_record(user_id)

@records_router.get("/get/book/{book_id}", status_code=200)
async def get_book_record_endpoint(book_id: str):
    return record_crud.get_book_record(book_id)

@records_router.get("/get/{record_id}", status_code=200)
async def get_record_endpoint(record_id: str):
    return record_crud.get_record(record_id)