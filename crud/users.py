from db import dummy


async def getProfile(userId):
    filtered_data = []
    for item in dummy.user_data:
        if item["id"] == userId:
            filtered_data.append(item)
    return filtered_data[0]


async def getReservation(userId):
    filtered_data = []
    temp = ''
    for item in dummy.user_data:
        if item["id"] == userId:
            temp = item['name']
    for item in dummy.reservation_data:
        if item['name'] == temp:
            filtered_data.append(item)
    return filtered_data


async def createReservation(userId):
    return None


async def createUser(data):
    return None