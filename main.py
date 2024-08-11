import uvicorn
from fastapi import FastAPI

from config import app_config
from src.stock_data.router import stocks_router
from src.stocks_aws.router import upload_router

app = FastAPI(**app_config)
app.include_router(stocks_router)
app.include_router(upload_router)


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8083, reload=True)
