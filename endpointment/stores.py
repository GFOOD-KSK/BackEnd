from typing import List
from fastapi import APIRouter
import schema.stores
import crud.stores

router = APIRouter()


@router.get("", response_model=List[schema.stores.Store])
async def get_stores(neLat: float, neLng: float, swLat: float, swLng: float, business_type: str):
    return await crud.stores.getStores(neLat, neLng, swLat, swLng, business_type)


@router.get("/{store_id}/menu", response_model=List[schema.stores.MenuOverlayItem])
async def get_store_menu(store_id: int):
    return await crud.stores.getStoresMenu(store_id)
     
@router.get("/{store_id}/reservation", response_model=List[schema.stores.getUserReservation])
async def get_users_reservation(store_id: int):
    return await crud.stores.getUsersReservation(store_id)

@router.get("/{food_type}", response_model=List[schema.stores.SearchItem])
async def get_stores_item(food_type: str):
    return await crud.stores.getStoresItem(food_type)
     