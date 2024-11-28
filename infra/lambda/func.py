import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Table_VisitorsCount')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'visitor_count'
    })
    views = response['Item']['visitor_count']
    views = views + 1
    print(views)
    response = table.put_item(Item={
            'id':'visitor_count',
            'visitor_count': views
    })

    return views