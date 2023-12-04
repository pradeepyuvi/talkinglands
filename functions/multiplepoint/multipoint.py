import json
import boto3

def lambda_handler(event, context):

    body = json.loads(event['body'])

    spatial_data = body.get('spatial_data')

    result = process_spatial_data(spatial_data)

    response = {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }

    return response

def process_spatial_data(spatial_data):

    spatial_data_store = []

    spatial_data_store.append(spatial_data)

    return 'Spatial data processed successfully'
