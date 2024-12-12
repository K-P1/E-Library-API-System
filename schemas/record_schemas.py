from pydantic import BaseModel
from typing import Optional
from datetime import date as dt_date

class WriteBorrowRecord(BaseModel):
    user_id: str
    book_id: str
    borrowed_at: Optional[dt_date] = dt_date.today()

class ReadBorrowRecord(WriteBorrowRecord):
    id: str
    returned_at: Optional[dt_date] = None

class UpdateBorrowRecord(BaseModel):
    returned_at: Optional[dt_date] = None

records: dict[str, ReadBorrowRecord] = {}