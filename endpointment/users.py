from db import dummy
from fastapi import APIRouter
from crud.users import Users


router = APIRouter()

@router.get("/users/{userId}")
async def get_profile(userId : int):
    result = await Users.getProfile(userId)
    return result

@router.get("/users/{userId}/reservation")
async def get_reservation(userId : int):
    result = await Users.getReservation(userId)
    return result
