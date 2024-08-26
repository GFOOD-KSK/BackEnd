import aiomysql
from fastapi import HTTPException
from schema.stores import Store
from db.session import get_connection
from data_mapping.stores import type_map

async def getStores(neLat: float, neLng: float, swLat: float, swLng: float, business_type: str):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
                SELECT idx, name, lat, lng, business_type
                FROM stores 
                WHERE business_type = %s 
                  AND lat BETWEEN %s AND %s
                  AND lng BETWEEN %s AND %s
                  
            """
            print(business_type)
            await cursor.execute(sql, (business_type, swLat, neLat, swLng, neLng))
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
                        y_coordinate=y_coordinate,
                        business_type=row["business_type"]
                    )
                    stores.append(store)
                return stores
            else:
                raise HTTPException(status_code=404, detail="Stores not found")
    finally:
        connection.close()


async def getStoresMenu(store_id):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
                    SELECT stores.name AS store_name, menus.name AS menu_name, stores.lat AS x_coordinate, stores.lng AS y_coordinate, stores.food_type AS food_type, stores.business_type AS business_type
                    FROM stores
                    JOIN menus ON stores.idx = menus.store_idx
                    WHERE stores.idx = %s
                """
            await cursor.execute(sql, (store_id,))
            result = await cursor.fetchall()
            print(result)
        if not result:
            raise HTTPException(status_code=404, detail="Store not found")

        return [
            {"store_name": temp["store_name"], "menu_name": temp["menu_name"], "x_coordinate": temp["x_coordinate"], "y_coordinate": temp["y_coordinate"], "food_type": temp["food_type"], "business_type": temp["business_type"]}
            for temp in result
        ]

    finally:
        connection.close()
async def getStoresItem(food_type):
    connection = await get_connection()
    try:
        food_type = type_map.get(food_type, '')
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            # 주어진 food_type에 따라 필터링
            sql = """
                    SELECT stores.name AS store_name, menus.name AS menu_name, menus.price, stores.idx
                    FROM stores
                    JOIN menus ON stores.idx = menus.store_idx
                    WHERE menus.food_type = %s
                """
            # food_type을 쿼리 파라미터로 전달
            await cursor.execute(sql, (food_type,))
            result = await cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No matching stores found")

            return [
                {"store_name": menu["store_name"], "menu_name": menu["menu_name"], "price": menu["price"]}
                for menu in result
            ]

    finally:
        connection.close()


async def getUsersReservation(store_id):
    connection = await get_connection()
    try:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            sql = """
                    SELECT idx, user_idx, reservation_at
                    FROM reservations
                    WHERE store_idx = %s
                """
            await cursor.execute(sql, (store_id,))
            result = await cursor.fetchall()

        if not result:
                raise HTTPException(status_code=404, detail="user not found")

        return [
            {"reservation_idx": item["idx"], "user_idx": item["user_idx"], "reservation_at": item["reservation_at"] }
            for item in result
        ]    
    
    finally:
        connection.close()
