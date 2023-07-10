from fastapi import APIRouter 

user_index = APIRouter(
    prefix="/user",
    tags= [
        "users",
    ]
)

@user_index.post("/register_user") 
async def register_user():
    return {
        "data": 1
    }