import datetime
from pydantic import BaseModel, validator
class User(BaseModel): # 기본 모델
    id: int
    kakao_id: int
    name: str
    email: str
    call: str
    type: str
    createdAt: str
    deleteAt: str

class getUserProfile(BaseModel): # 프로필 모델
    name: str
    email: str
    call: str
    type: str
   
class postUser(BaseModel): # 유저 생성 모델
    kakao_id: int
    name: str
    email: str
    call: str
    type: str

class Reservation(BaseModel): # 예약 기본 모델
    id: int
    user_idx: int
    store_idx: int
    reservationAt: str

 
class getReservation(BaseModel): # 예약 확인 모델
    store_name: str
    business_type : str
    food_type : str
    reservationAt: str
    

class postReservation(BaseModel): # 예약 생성 모델
    user_idx: int
    store_idx: int

    


