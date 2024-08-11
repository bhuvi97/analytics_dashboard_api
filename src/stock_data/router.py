from fastapi import APIRouter
from stock_data import service

stocks_router = APIRouter(prefix="/stocks", tags=["upload"])


@stocks_router.get('')
async def get_stocks():
    return await service.get_stock_data()
