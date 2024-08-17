from typing import List
from fastapi import APIRouter, HTTPException
import crud.users
import schema.users
import re
router = APIRouter()


@router.get("/{userId}", response_model =schema.users.getUserProfile)  # 더미데이터 -> DB로 변경
async def get_profile(userId: int):
    return await crud.users.getProfile(userId)



@router.post("")  # 세부구현
async def create_profile(data: schema.users.postUser):
    """
    todo: 입력값 검증 문제있음.
    :param data:
    :return:
    """
    #if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data.email): raise HTTPException(status_code=400, detail="Invalid Requests")
    #if re.match("^\d{3}-\d{4}-\d{3}$", data.call): raise HTTPException(status_code=400, detail="Invalid Requests")
    res = await crud.users.createUser(data)
    return {'success': True, 'data': res}


@router.post("/{userId}/reservation")  # 세부구현
async def create_reservation(data: schema.users.postReservation):
    return await crud.users.createReservation(data)


@router.get("/{userId}/reservation", response_model = List[schema.users.getReservation])  # 더미데이터 -> DB로 변경
async def get_reservation(userId: int):
    return await crud.users.getReservation(userId)

