from db import dummy
from typing import List, Optional
from fastapi import APIRouter
import crud.users
import schema.users
router = APIRouter()


@router.get("/{userId}", response_model =schema.users.User)  # 더미데이터 -> DB로 변경
async def get_profile(userId: int):
    result = await crud.users.getProfile(userId)
    print(result)
    return result


@router.post("/{userId}", response_model =schema.users.User)  # 세부구현
async def create_profile(data: schema.users.User):
    return await crud.users.createUser(data)



@router.get("/{userId}/reservation", response_model = List[schema.users.Reservation])  # 더미데이터 -> DB로 변경
async def get_reservation(userId: int):
    result = await crud.users.getReservation(userId)
    return result


@router.post("/{userId}/reservation", response_model =schema.users.Reservation)  # 세부구현
async def create_reservation(userId: int):
    return await crud.users.createReservation(userId)
