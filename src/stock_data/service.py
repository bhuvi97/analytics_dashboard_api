from httpx import AsyncClient
from . import config as stock_config

"""
?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=EGI4IVDOQYEZCUPI
"""

async def get_stock_data():
    async with AsyncClient() as client:
        response = await client.get(url=stock_config.ALPHAVANTAGE_ENDPOINT, params={
            "function": "TIME_SERIES_DAILY",
            "symbol": "IBM",
            "interval": "5min",
            "apikey": stock_config.ALPHAVANTAGE_API_KEY
        })
        return response