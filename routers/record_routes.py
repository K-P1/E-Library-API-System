from fastapi import APIRouter, HTTPException
from crud.record_crud import record_crud
from datetime import date as dt_date
from typing import Optional

from schemas.record_schemas import UpdateRecord

records_router = APIRouter()

@records_router.post("/create", status_code=201)
async def create_record_endpoint(user_id: str, book_id: str):
    record = record_crud.create_record(user_id, book_id)
    return record

@records_router.get("/get/{record_id}", status_code=200)
async def get_record_endpoint(record_id: str):
    record = record_crud.get_record(record_id)
    return record

@records_router.get("/get/all", status_code=200)
async def get_all_records_endpoint():
    return record_crud.get_all_records()

@records_router.patch("/update/{record_id}", status_code=200)
async def update_record_endpoint(record_id: str, returned_at: Optional[dt_date]):
    update_data = UpdateRecord(returned_at=returned_at)
    return record_crud.update_record(record_id, update_data)