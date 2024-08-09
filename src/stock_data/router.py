from fastapi import APIRouter
from stock_data import service

stocks_router = APIRouter(prefix="/stocks", tags=["stocks"])


@stocks_router.get('')
async def get_stocks():
    k = 1
    return await service.get_stock_data()
