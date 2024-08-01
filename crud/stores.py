import aiomysql
from fastapi import HTTPException
from schema.stores import Store
from db.session import get_connection

class Stores:
    async def getStores():
        connection = await get_connection()
        try:
            async with connection.cursor(aiomysql.DictCursor) as cursor:
                sql = "SELECT idx, name, lat, lng, business_type FROM stores limit 1000"
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
                sql = "SELECT name, price FROM menus WHERE store_idx = %s"
                await cursor.execute(sql, (store_id,))
                result = await cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Store not found")

            
            return [
                {"name": menu["name"], "price": menu["price"]} 
                for menu in result
            ]
        
        finally:
            connection.close()

    async def getStoresItem(food_type):
        connection = await get_connection()
        try:
            type_map = {
                '한식': 'a',
                '중식': 'b',
                '일식': 'c',
                '양식': 'd',
                '패스트푸드': 'e',
                '일반대중음식': 'f',
                '편의점': 'g',
                '제과점': 'h'
            }

            food_type = type_map.get(food_type, '')

            async with connection.cursor(aiomysql.DictCursor) as cursor:
                # 주어진 food_type에 따라 필터링
                sql = """
                    SELECT stores.name AS store_name, menus.name AS menu_name, menus.price
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
