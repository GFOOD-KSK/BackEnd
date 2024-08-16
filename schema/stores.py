from pydantic import BaseModel


class Store(BaseModel):
    idx : int
    name : str
    x_coordinate : float
    y_coordinate : float
    business_type : str
    # food_type : str
    # call : str

class MenuItem(BaseModel):
    idx: int
    store_idx: int
    name: str
    price: int
    food_type : str

class MenuOverlayItem(BaseModel): # 오버레이 조회
    store_name: str
    menu_name: str
    x_coordinate: float
    y_coordinate: float
    food_type: str
    business_type: str

class SearchItem(BaseModel):
    store_name: str
    menu_name: str
    price: float

class getUserReservation(BaseModel):
    reservation_idx : int
    user_idx: int
    reservationAt : str