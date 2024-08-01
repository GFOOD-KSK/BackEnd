import aiomysql
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from db.session import get_connection
from schema.stores import MenuOverlayItem, SearchItem, Store
from crud.stores import Stores

router = APIRouter()


@router.get("/stores", response_model=List[Store])
async def get_stores():
    result = await Stores.getStores()
    return result

@router.get("/stores/{store_id}/menu", response_model=List[MenuOverlayItem])
async def get_store_menu(store_id: int, detailed: Optional[bool] = Query(False)):
    result = await Stores.getStoresMenu(store_id)
    return result


@router.get("/stores/{food_type}", response_model=List[SearchItem])
async def get_stores_item(food_type: str, detailed: Optional[bool] = Query(False)):
    result = await Stores.getStoresItem(food_type)
    return result