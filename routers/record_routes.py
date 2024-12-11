from fastapi import APIRouter
from crud.record_crud import record_crud
from schemas.record_schemas import WriteBorrowRecord
from datetime import date as dt_date
from typing import Optional

from schemas.record_schemas import UpdateBorrowRecord

records_router = APIRouter()

@records_router.post("/create", status_code=201)
async def create_record_endpoint(data: WriteBorrowRecord):
    record = record_crud.create_record(data)
    return record

@records_router.get("/get/{record_id}", status_code=200)
async def get_record_endpoint(record_id: str):
    record = record_crud.get_record(record_id)
    return record

@records_router.get("/get/all", status_code=200)
async def get_all_records_endpoint():
    return record_crud.get_all_records()

@records_router.patch("/update/{record_id}", status_code=200)
async def update_record_endpoint(
    record_id: str, 
    returned_at: UpdateBorrowRecord):
    update_data = record_crud.update_record(record_id, returned_at)
    return update_data