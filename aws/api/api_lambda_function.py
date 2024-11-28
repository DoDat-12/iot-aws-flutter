import boto3
import os
import json
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'WeatherData_v3'

# Helper function to convert Decimal to standard Python types


def decimal_to_float(obj):
    if isinstance(obj, list):
        return [decimal_to_float(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: decimal_to_float(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)  # Convert Decimal to float
    else:
        return obj


def lambda_handler(event, context):
    table = dynamodb.Table(table_name)

    try:
        # Retrieve all data from the table
        response = table.scan()
        items = response.get('Items', [])

        # Convert Decimal values to standard types
        items = decimal_to_float(items)

        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        print(f"Error fetching data from DynamoDB: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
