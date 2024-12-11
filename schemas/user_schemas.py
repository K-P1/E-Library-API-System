from pydantic import BaseModel
from typing import Optional

class WriteUser(BaseModel):
    name: str
    email: str
    is_active: Optional[bool] = True

class ReadUser(WriteUser):
    id: str
    class ConfigDict:
        from_attributes: True
        exclude_unset: True

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True

users: dict[str, ReadUser] = {}