import json
import time
import math
import boto3
from botocore.exceptions import ClientError
import os

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]

def handler(event, context):
    params = event.get("queryStringParameters") or {}
    mode = params.get("mode", "normal")

    if mode == "error":
        raise Exception("Intentional error for POC")

    if mode == "db_down":
        try:
            table = dynamodb.Table(TABLE_NAME)
            table.get_item(Key={"pk": "nonexistent"})
        except ClientError as e:
            raise Exception(f"Simulated DB outage: {e}")

    if mode == "cpu_stress":
        end = time.time() + 5
        x = 0.0001
        while time.time() < end:
            x = math.sqrt(x * x + 1.2345)

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item={"pk": "demo", "mode": mode, "ts": int(time.time())})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK", "mode": mode})
    }
