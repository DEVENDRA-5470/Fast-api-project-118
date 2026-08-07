from pydantic import BaseModel
from typing import Optional

class StaffCreate(BaseModel):
    emp_name: str
    emp_age: int
    emp_city: str

class StaffUpdate(BaseModel):
    emp_name: Optional[str] = None
    emp_age: Optional[int] = None
    emp_city: Optional[str] = None