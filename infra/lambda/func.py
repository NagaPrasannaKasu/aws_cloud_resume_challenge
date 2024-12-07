import json
import boto3 # type: ignore
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Visitors_Table')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'visitor_count'
    })
    views = response['Item']['visitors']
    views = views + 1
    print(views)
    response = table.put_item(Item={
            'id':'visitor_count',
            'visitors': views
    })
    responseBody = json.dumps(int(views))
    
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": responseBody
    }

    return apiResponse

    