from fastapi import APIRouter
from schemas.user import UserRegister
from models.user import User
from utils.security import hash_password

router=APIRouter(
    prefix="/auth",
    tags=["Authencation"]
)

@router.post("/register")
async def register(user: UserRegister):
    
    hashed_password=hash_password(user.password)
    new_user=User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hashed_password
    )
    
    new_user.save()
    
    return {
        "message":"User Registered Successfully ✅",
        "User_id":str(new_user.id)
    }
    
