import aiomysql
from config import DATABASE
async def get_connection():
    connection = await aiomysql.connect(
        host=DATABASE['host'],
        port=DATABASE['port'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        db=DATABASE['db'],
    )
    return connection
