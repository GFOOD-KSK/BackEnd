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
    name: str
    price: int

class SearchItem(BaseModel):
    store_name: str
    menu_name: str
    price: float