from datetime import datetime
import aiomysql
from fastapi import HTTPException
from db.session import get_connection


async def getProfile(kakaoId):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = "SELECT idx FROM users WHERE kakao_id = %s"
            await cursor.execute(sql, (kakaoId,))
            result = await cursor.fetchall()
            result = result[0]

        if not result:
            raise HTTPException(status_code=404, detail="user not found")

        return result['idx']
    finally:
        connection.close()


async def createUser(data):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
            INSERT INTO users (kakao_id, name, email, `call`, type, created_at) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await cursor.execute(sql, (data.kakao_id, data.name, data.email, data.call, data.type, nowTime))

            await connection.commit()

            await cursor.execute("SELECT LAST_INSERT_ID()")

            last_id = await cursor.fetchone()

            return last_id
    finally:
        connection.close()

