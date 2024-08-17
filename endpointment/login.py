import os

from starlette.responses import RedirectResponse

KAKAO_CLIENT_ID = 'cde0cad67453d3b9fb93961a730ab660'
KAKAO_REDIRECT_URI = 'http://127.0.0.1:8002/auth/kakao/callback'

from fastapi import APIRouter, HTTPException, Query, Request
from typing import List, Optional
import requests

router = APIRouter()


@router.get("/kakao/callback")
async def kakao_callback(request: Request, code: str):
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_CLIENT_ID,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": code,
    }
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    token_json = token_response.json()

    access_token = token_json.get("access_token")
    if access_token:
        # 액세스 토큰을 사용해 사용자 정보 요청
        user_info_url = "https://kapi.kakao.com/v2/user/me"
        user_info_headers = {
            "Authorization": f"Bearer {access_token}"
        }
        user_info_response = requests.get(user_info_url, headers=user_info_headers)
        user_info = user_info_response.json()

        # 사용자 정보를 세션에 저장
        request.session['user'] = user_info
        print(request.session)

        # 리다이렉트 또는 사용자 정보 반환
        return RedirectResponse(url='http://127.0.0.1:5500/index.html')
    else:
        return {"error": "Failed to get access token"}


@router.get('/login')
async def login():
    return {}

@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return ({"message": "Logged out"})
