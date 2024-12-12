from pydantic import BaseModel
from typing import Optional

class WriteUser(BaseModel):
    name: str
    email: str
    is_active: Optional[bool] = True

class ReadUser(WriteUser):
    id: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

class FullUpdateUser(BaseModel):
    name: str
    email: str
    is_active: bool

users: dict[str, ReadUser] = {}