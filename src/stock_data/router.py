from fastapi import APIRouter
from . import service

stocks_router = APIRouter(prefix="/stocks", tags=["stocks"])


@stocks_router.get('')
async def get_stocks():
    return service.get_stock_data()
