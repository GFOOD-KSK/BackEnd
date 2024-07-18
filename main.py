from fastapi import FastAPI, HTTPException
from typing import List
from database import get_connection
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import aiomysql
import dummy

restaurantData = dummy.restaurant_data
reservationData = dummy.reservation_data
userData = dummy.user_data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",  # React 등의 프론트엔드 개발 서버
    "http://yourfrontenddomain.com",  # 실제 프론트엔드 도메인
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Store(BaseModel):
    idx: int
    name: str
    x_coordinate: float
    y_coordinate: float
    type: str


class MenuItem(BaseModel):
    idx: int
    store_idx: int
    name: str
    price: int

@app.get("/stores", response_model=List[Store])
async def get_stores():
    return [Store(**row) for row in dummy.store]


@app.get("/stores/{store_id}/menu", response_model=List[MenuItem])
async def get_store_menu(store_id: int):
    result = []
    for i in dummy.menus:
        if i['store_idx'] == store_id:
            result.append(i)

    return [MenuItem(**row) for row in result]


@app.get("/stores/{searchData}")
async def get_stores_item(searchData : str):
    filtered_data = []
    for item in restaurantData:
        if item["classification"] == searchData:
            filtered_data.append(item)
    return filtered_data

@app.get("/users/{userId}")
async def get_profile(userId : int):
    filtered_data = []
    for item in userData:
        if item["id"] == userId:
            filtered_data.append(item)
    return filtered_data

@app.get("/users/{userId}/reservation")
async def get_reservation(userId : int):
    filtered_data = []
    temp = ''
    for item in userData:
        if item["id"] == userId:
            temp = item['name']
    for item in reservationData:
        if item['name'] == temp:
            filtered_data.append(item)
    return filtered_data
