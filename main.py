import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from endpointment import stores, users, login

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='1412', same_site="None", https_only=False)

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

app.include_router(stores.router, prefix="/stores", tags=["stores"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(login.router, prefix="/auth", tags=["login"])