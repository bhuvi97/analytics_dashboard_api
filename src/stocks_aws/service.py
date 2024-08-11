import boto3
import datetime

from stock_data.service import get_stock_data

# TODO upload the data from api to s3 bucket as csv files


async def upload_csv():
    client = boto3.client('s3')
    stock_data = await get_stock_data()
    try:
        client.put_object(
            Body=stock_data,
            Bucket='bhuvi-bucket',
            Key=f"stocks_data{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv",
        )
    except Exception as e:
        print(e)

"""
kxMQv33!CNCgKwVuPJpeizK*qT
"""