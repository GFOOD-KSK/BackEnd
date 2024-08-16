from datetime import datetime
import aiomysql
from fastapi import HTTPException
from db.session import get_connection

async def getProfile(userId):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = "SELECT name, email, `call`, idx FROM users WHERE idx = %s"
            await cursor.execute(sql, (userId,))
            result = await cursor.fetchall()
            result = result[0]

        if not result:
            raise HTTPException(status_code=404, detail="user not found")

        return {"name": result["name"], "email": result["email"], "call": result["call"], "idx": result["idx"] }
            
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
            await cursor.execute(sql, (data.kakao_id, data.name, data.email, data.call, data.type, nowTime ))

            await connection.commit()
            
            await cursor.execute("SELECT LAST_INSERT_ID()")
            
            last_id = await cursor.fetchone()

            return last_id
    finally:
        connection.close()

async def getReservation(userId):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
                    SELECT stores.name AS store_name, stores.business_type AS business_type, stores.food_type As food_type, reservations.reservation_at AS reservation_at
                    FROM reservations
                    JOIN stores ON reservations.store_idx = stores.idx
                    JOIN users ON users.idx = reservations.user_idx
                    WHERE users.idx = %s
                """
            await cursor.execute(sql, (userId,))
            result = await cursor.fetchall()
            print(result)
        if not result:
                raise HTTPException(status_code=404, detail="user not found")

        return [
            {"store_name": item["store_name"], "business_type": item["business_type"], "food_type": item["food_type"], "reservationAt": item["reservation_at"] }
            for item in result
        ]    
    
    finally:
        connection.close()


async def createReservation(data):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
            INSERT INTO reservations (user_Idx, store_idx, reservation_at) 
            VALUES (%s, %s, %s)
            """
            nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await cursor.execute(sql, (data.user_idx, data.store_idx, nowTime))

            await connection.commit()
            
            await cursor.execute("SELECT LAST_INSERT_ID()")
            
            last_id = await cursor.fetchone()

            return last_id

    finally:
        connection.close()


