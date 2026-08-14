from fastapi import APIRouter,Depends,status
from models.destination import Destination
from models.user import User
from schemas.destination import DestinationCreate,DestinationResponse

from dependencies.auth import get_current_user

router=APIRouter(
    prefix="/destinations",
    tags=["Destination"]
)

@router.post("/",response_model=list[DestinationCreate])
async def create_destination(destination:DestinationCreate, currrent_user :User=Depends(get_current_user)):
    new_destination=Destination(
        name=destination.name,
        location=destination.location,
        description=destination.description,
        price=destination.price,
        duration=destination.duration,
        image=destination.image,
        activities=destination.activities
    )
    
    new_destination.save()
    
    return {
        "id":str(new_destination.id),
        "name":new_destination.name,
        "location":new_destination.location,
        "description":new_destination.description,
        "price":new_destination.price,
        "duration":new_destination.duration,
        "image":new_destination.image,
        "activities":new_destination.activities
        
    }
    
    
@router.get("/",response_model=list[DestinationResponse])
async def get_destination():
    destinations=Destination.objects.all()
    return[{
        "id":str(destination.id),
        "name":destination.name,
        "location":destination.location,
        "description":destination.description,
        "price":destination.price,
        "duration":destination.duration,
        "image":destination.image,
        "activities":destination.activities
        
    }
    for destination in destinations   
    ]
        