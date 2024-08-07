from datetime import datetime
import aiomysql
from fastapi import HTTPException
from db.session import get_connection

async def getProfile(userId):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = "SELECT name, email, `call`, type FROM users WHERE idx = %s"
            await cursor.execute(sql, (userId,))
            result = await cursor.fetchall()
            result = result[0]

        if not result:
            raise HTTPException(status_code=404, detail="user not found")

        return {"name": result["name"], "email": result["email"], "call": result["call"], "type": result["type"] }
            
    finally:
        connection.close()

async def createUser(data):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
            INSERT INTO users (kakao_id, name, email, `call`, type, createdAt) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await cursor.execute(sql, (data.kakao_id, data.name, data.email, data.call, data.type, nowTime ))

            await connection.commit()
            
            return "success"

    finally:
        connection.close()

async def getReservation(userId):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
                    SELECT stores.name AS store_name, stores.business_type AS business_type, stores.food_type As food_type, reservations.reservationAt AS reservationAt
                    FROM reservations
                    JOIN stores ON reservations.store_idx = stores.idx
                    JOIN users ON users.idx = reservations.user_idx
                    WHERE users.idx = %s
                """
            await cursor.execute(sql, (userId,))
            result = await cursor.fetchall()

        if not result:
                raise HTTPException(status_code=404, detail="user not found")

        return [
            {"store_name": item["store_name"], "business_type": item["business_type"], "food_type": item["food_type"], "reservationAt": item["reservationAt"] }
            for item in result
        ]    
    
    finally:
        connection.close()


async def createReservation(data):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
            INSERT INTO reservations (user_Idx, store_idx, reservationAt) 
            VALUES (%s, %s, %s)
            """
            nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await cursor.execute(sql, (data.user_idx, data.store_idx, nowTime))

            await connection.commit()
            
            return "success"

    finally:
        connection.close()


