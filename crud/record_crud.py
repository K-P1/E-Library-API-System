from schemas.record_schemas import ReadBorrowRecord, UpdateBorrowRecord, WriteBorrowRecord, records
from fastapi import HTTPException
from datetime import date as dt_date

def add_record(data: WriteBorrowRecord):
    new_id = f"rc_{str(len(records) + 1).zfill(4)}"
    record = ReadBorrowRecord(
        id=new_id, 
        user_id= data.user_id, 
        book_id= data.book_id, 
        borrowed_at= data.borrowed_at)
    records[new_id] = record
    return record

class RecordCrud:
    @staticmethod
    def create_record(data: WriteBorrowRecord):
        record = add_record(data)
        return record

    @staticmethod
    def get_record(record_id: str):
        record = records.get(record_id)
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        return record

    @staticmethod
    def get_all_records():
        return list(records.values())

    @staticmethod
    def update_record(record_id: str, update_data: UpdateBorrowRecord):
        record = records.get(record_id)
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        if update_data.returned_at:
            record.returned_at = update_data.returned_at
        records[record_id] = record
        return record

record_crud = RecordCrud()