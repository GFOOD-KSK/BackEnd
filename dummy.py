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
menus = []
for i in range(1, 101):
    menu = {
        "idx" : i,
        "store_idx": (i % 10) + 1,  # This will ensure store_id ranges from 1 to 10
        "name": f"menu{i}",
        "price": 1000 + (i * 100)  # Prices incrementing by 100 starting from 1000
    }
    menus.append(menu)