from pydantic import BaseModel
from typing import Optional

class WriteBook(BaseModel):
    title: str
    author: str
    is_available: Optional[bool] = True

class ReadBook(WriteBook):
    id: str

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = True

books: dict[str, ReadBook] = {}