from pydantic import BaseModel

class StaffCreate(BaseModel):
    emp_name: str
    emp_age: int
    emp_city: str