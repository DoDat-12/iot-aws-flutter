import boto3


def lambda_handler(event, context):
    """
    Send data into DynamoDB
    """
    client = boto3.client('dynamodb')

    response = client.put_item(
        TableName='WeatherData_v3',
        Item={
            'temperature': {'N': str(event['temperature'])},
            'humidity': {'N': str(event['humidity'])},
            'timestamp': {'S': event['timestamp']}
        }
    )

    return 0

# { "temperature" : { "N" : "29.3" }, "humidity" : { "N" : "64" }, "timestamp" : { "S" : "08-11-2024 16:47:23" } }
