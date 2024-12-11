from pydantic import BaseModel
from typing import Optional
from datetime import date as dt_date

class Record(BaseModel):
    user_id: str  # Ensure user_id is a string to match in-memory constraints
    book_id: str  # book_id should also match this data type
    borrowed_at: dt_date
    returned_at: Optional[dt_date] = None  # Optional as the book may not be returned yet

class ReadRecord(Record):
    id: str
    class ConfigDict:
        from_attributes: True
        exclude_unset: True

class UpdateRecord(BaseModel):
    returned_at: Optional[dt_date] = None

records: dict[str, ReadRecord] = {}

# Record generation logic (dynamically expandable)
def add_record(user_id: str, book_id: str):
    new_id = f"rc_{str(len(records) + 1).zfill(4)}"
    record = ReadRecord(id=new_id, user_id=user_id, book_id=book_id, borrowed_at=dt_date.today())
    records[new_id] = record
    return record