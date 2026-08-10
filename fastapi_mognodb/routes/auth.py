from fastapi import APIRouter
from schemas.user import UserRegister
from models.user import User

router=APIRouter(
    prefix="/auth",
    tags=["Authencation"]
)

@router.post("/register")
async def register(user: UserRegister):
    new_user=User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=user.password
    )
    
    new_user.save()
    
    return {
        "message":"User Registered Successfully ✅",
        "User_id":str(new_user.id)
    }
    
@router.post("/get-users")
async def get_user():
    
     return {
            "message":"Get Successfully ✅" 
        }