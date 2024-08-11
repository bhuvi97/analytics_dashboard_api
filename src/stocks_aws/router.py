from fastapi import APIRouter
from stocks_aws.service import upload_csv

upload_router = APIRouter(prefix="/upload", tags=["stocks"])


@upload_router.get('', status_code=201)
async def upload_stocks():
    return await upload_csv()
