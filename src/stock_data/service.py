from httpx import AsyncClient
from stock_data import config as stock_config


async def get_stock_data():
    async with AsyncClient() as client:
        response = await client.get(url=stock_config.ALPHAVANTAGE_ENDPOINT, params={
            "function": "TIME_SERIES_DAILY",
            "symbol": "IBM",
            "apikey": stock_config.ALPHAVANTAGE_API_KEY,
            "datatype": "csv"
        })
        return response.text
