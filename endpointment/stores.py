import aiomysql
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from db.session import get_connection
import schema.stores
import crud.stores

router = APIRouter()


@router.get("", response_model=schema.stores.Store)
async def get_stores(neLat: float, neLng: float, swLat: float, swLng: float, business_type: str):
    result = await crud.stores.getStores(neLat, neLng, swLat, swLng, business_type)
    return result

@router.get("/{store_id}/menu", response_model=schema.stores.MenuItem)
async def get_store_menu(store_id: int, detailed: Optional[bool] = Query(False)):
    result = await crud.stores.getStoresMenu(store_id)
    return result


@router.get("/{food_type}", response_model=schema.stores.SearchItem)
async def get_stores_item(food_type: str, detailed: Optional[bool] = Query(False)):
    result = await crud.stores.getStoresItem(food_type)
    return result