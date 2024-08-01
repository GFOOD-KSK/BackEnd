from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
class Reservation(BaseModel):
    userIdx: int
    name: str
    reservation_datetime: str
    store_name: str
    store_idx: int
