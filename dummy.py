store = [
    {"idx": 1, "y_coordinate": 129.7631, "x_coordinate": 33.0457, "name": "store1", "type": "일식집"},
    {"idx": 2, "y_coordinate": 126.9421, "x_coordinate": 33.9325, "name": "store2", "type": "한식집"},
    {"idx": 3, "y_coordinate": 128.2735, "x_coordinate": 36.2258, "name": "store3", "type": "분식집"},
    {"idx": 4, "y_coordinate": 125.5651, "x_coordinate": 36.8231, "name": "store4", "type": "일식집"},
    {"idx": 5, "y_coordinate": 128.3239, "x_coordinate": 37.5440, "name": "store5", "type": "일식집"},
    {"idx": 6, "y_coordinate": 125.0111, "x_coordinate": 34.0844, "name": "store6", "type": "일식집"},
    {"idx": 7, "y_coordinate": 128.2505, "x_coordinate": 33.0593, "name": "store7", "type": "일식집"},
    {"idx": 8, "y_coordinate": 127.9296, "x_coordinate": 35.5582, "name": "store8", "type": "일식집"},
    {"idx": 9, "y_coordinate": 126.8547, "x_coordinate": 37.1960, "name": "store9", "type": "일식집"},
    {"idx": 10, "y_coordinate": 130.1344, "x_coordinate": 33.5387, "name": "store10", "type": "고기집"}
    ]
restaurant_data = [
    {"name": "Store 1", "menu_name": "김치찌개", "menu_price": 12000, "classification": "한식"},
    {"name": "Store 1", "menu_name": "비빔밥", "menu_price": 10000, "classification": "한식"},
    {"name": "Store 2", "menu_name": "짜장면", "menu_price": 15000, "classification": "중식"},
    {"name": "Store 2", "menu_name": "짬뽕", "menu_price": 13000, "classification": "중식"},
    {"name": "Store 3", "menu_name": "초밥", "menu_price": 18000, "classification": "일식"},
    {"name": "Store 3", "menu_name": "라멘", "menu_price": 20000, "classification": "일식"},
    {"name": "Store 4", "menu_name": "스테이크", "menu_price": 22000, "classification": "양식"},
    {"name": "Store 4", "menu_name": "파스타", "menu_price": 25000, "classification": "양식"},
    {"name": "Store 5", "menu_name": "불고기", "menu_price": 12000, "classification": "한식"},
    {"name": "Store 5", "menu_name": "비빔국수", "menu_price": 11000, "classification": "한식"},
    {"name": "Store 6", "menu_name": "탕수육", "menu_price": 13000, "classification": "중식"},
    {"name": "Store 6", "menu_name": "볶음밥", "menu_price": 14000, "classification": "중식"},
    {"name": "Store 7", "menu_name": "초밥", "menu_price": 16000, "classification": "일식"},
    {"name": "Store 7", "menu_name": "우동", "menu_price": 17000, "classification": "일식"},
    {"name": "Store 8", "menu_name": "스테이크", "menu_price": 20000, "classification": "양식"},
    {"name": "Store 8", "menu_name": "파스타", "menu_price": 18000, "classification": "양식"},
    {"name": "Store 9", "menu_name": "된장찌개", "menu_price": 13000, "classification": "한식"},
    {"name": "Store 9", "menu_name": "갈비탕", "menu_price": 15000, "classification": "한식"},
    {"name": "Store 10", "menu_name": "짜장면", "menu_price": 14000, "classification": "중식"},
    {"name": "Store 10", "menu_name": "짬뽕", "menu_price": 16000, "classification": "중식"},
]

reservation_data = [
    {"name": "John Doe", "reservation_datetime": "2024-07-15T10:30:00", "store_name": "Store A"},
    {"name": "John Doe", "reservation_datetime": "2024-07-25T10:30:00", "store_name": "Store K"},
    {"name": "Jane Smith", "reservation_datetime": "2024-07-16T12:00:00", "store_name": "Store B"},
    {"name": "Michael Johnson", "reservation_datetime": "2024-07-17T15:45:00", "store_name": "Store C"},
    {"name": "Emily Brown", "reservation_datetime": "2024-07-18T18:20:00", "store_name": "Store D"},
    {"name": "William Lee", "reservation_datetime": "2024-07-19T11:10:00", "store_name": "Store E"},
    {"name": "Sophia Wilson", "reservation_datetime": "2024-07-20T14:30:00", "name": "Store F"},
    {"name": "James Martinez", "reservation_datetime": "2024-07-21T17:00:00", "name": "Store G"},
    {"name": "Olivia Garcia", "reservation_datetime": "2024-07-22T19:15:00", "name": "Store H"},
    {"name": "Ethan Robinson", "reservation_datetime": "2024-07-23T13:40:00", "name": "Store I"},
    {"name": "Isabella Miller", "reservation_datetime": "2024-07-24T16:00:00", "name": "Store J"},
]
menus = []
for i in range(1, 101):
    menu = {
        "idx" : i,
        "store_idx": (i % 10) + 1,  # This will ensure store_id ranges from 1 to 10
        "name": f"menu{i}",
        "price": 1000 + (i * 100)  # Prices incrementing by 100 starting from 1000
    }
    menus.append(menu)

user_data = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "123-456-7890"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "phone": "234-567-8901"},
    {"id": 3, "name": "Michael Johnson", "email": "michael.johnson@example.com", "phone": "345-678-9012"},
    {"id": 4, "name": "Emily Brown", "email": "emily.brown@example.com", "phone": "456-789-0123"},
    {"id": 5, "name": "William Lee", "email": "william.lee@example.com", "phone": "567-890-1234"},
    {"id": 6, "name": "Sophia Wilson", "email": "sophia.wilson@example.com", "phone": "678-901-2345"},
    {"id": 7, "name": "James Martinez", "email": "james.martinez@example.com", "phone": "789-012-3456"},
    {"id": 8, "name": "Olivia Garcia", "email": "olivia.garcia@example.com", "phone": "890-123-4567"},
    {"id": 9, "name": "Ethan Robinson", "email": "ethan.robinson@example.com", "phone": "901-234-5678"},
    {"id": 10, "name": "Isabella Miller", "email": "isabella.miller@example.com", "phone": "012-345-6789"},
]
