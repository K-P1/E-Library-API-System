from schemas.record_schemas import ReadRecord, UpdateRecord, records, add_record
from fastapi import HTTPException

class RecordCrud:
    @staticmethod
    def create_record(user_id: str, book_id: str):
        record = add_record(user_id, book_id)
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
    def update_record(record_id: str, update_data: UpdateRecord):
        record = records.get(record_id)
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        if update_data.returned_at:
            record.returned_at = update_data.returned_at
        records[record_id] = record
        return record

record_crud = RecordCrud()