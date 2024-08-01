import aiomysql
from db.config import DATABASE

async def get_connection():
    try:
        connection = await aiomysql.connect(
            host=DATABASE['host'],
            port=DATABASE['port'],
            user=DATABASE['user'],
            password=DATABASE['password'],
            db=DATABASE['db'],
        )
        return connection
    except aiomysql.Error as e:
        print(f"Database connection error: {e}")
        return None
