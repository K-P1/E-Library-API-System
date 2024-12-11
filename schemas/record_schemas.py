from pydantic import BaseModel
from typing import Optional
from datetime import date as dt_date

class Record(BaseModel):
    user_id: str
    book_id: str
    borrowed_at: dt_date
    returned_at: Optional[dt_date] = None

class ReadRecord(Record):
    id: str
    class ConfigDict:
        from_attributes: True
        exclude_unset: True

class UpdateRecord(BaseModel):
    returned_at: Optional[dt_date] = None

records: dict[str, ReadRecord] = {}