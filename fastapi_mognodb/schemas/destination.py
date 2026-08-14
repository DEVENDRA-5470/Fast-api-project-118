from pydantic import BaseModel

class DestinationCreate(BaseModel):
    name: str
    location: str
    description:str
    price: float
    duration: int
    image: str
    activities: list[str] = []
    
class DestinationResponse(BaseModel):
    id:str
    name: str
    location: str
    description:str
    price: float
    duration: int
    image: str
    activities: list[str]