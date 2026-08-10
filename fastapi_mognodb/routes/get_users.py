from fastapi import APIRouter
from models.user import User

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
async def get_user():
    users=User.objects.all()
    return [{
        "id": str(user.id),
        "full_name":user.full_name,
        "email":user.email,
        "phone":user.phone
    }
     for user in users       
    ]