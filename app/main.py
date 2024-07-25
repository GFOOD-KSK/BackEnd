from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import aiomysql

from app.db import dummy
from app.db.database import get_connection

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



class MenuItem(BaseModel):
    idx: int
    store_idx: int
    name: str
    price: int

@app.get("/stores", response_model=List[Store])
async def get_stores():
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = "SELECT idx, name, lat, lng FROM stores limit 1000"
            await cursor.execute(sql)
            result = await cursor.fetchall()
            if result:
                stores = []
                for row in result:
                    # Handle None values
                    x_coordinate = row["lat"] if row["lat"] is not None else 0.0
                    y_coordinate = row["lng"] if row["lng"] is not None else 0.0
                    store = Store(
                        idx=row["idx"],
                        name=row["name"],
                        x_coordinate=x_coordinate,
                        y_coordinate=y_coordinate
                    )
                    stores.append(store)
                return stores
            else:
                raise HTTPException(status_code=404, detail="Stores not found")
    finally:
        connection.close()

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
    for item in dummy.menus:
        if item["classification"] == searchData:
            item['store_name'] = dummy.getStoreNameFromId(item['store_idx'])
            filtered_data.append(item)
    return filtered_data

@app.get("/users/{userId}")
async def get_profile(userId : int):
    filtered_data = []
    for item in dummy.user_data:
        if item["id"] == userId:
            filtered_data.append(item)
    return filtered_data

@app.get("/users/{userId}/reservation")
async def get_reservation(userId : int):
    filtered_data = []
    temp = ''
    for item in dummy.user_data:
        if item["id"] == userId:
            temp = item['name']
    for item in dummy.reservation_data:
        if item['name'] == temp:
            filtered_data.append(item)
    return filtered_data
