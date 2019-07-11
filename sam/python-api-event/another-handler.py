print('Loading Function')


def handler(event, context):
    print("Event: " + str(event))
    print("Method: " + event['httpMethod'])
    print("Path: " + event['resource'])
    print("Body: " + str(event['body']))

    method = event['httpMethod']
    if method == "GET":
        response = {
            "statusCode": 200,
            "body": "This is a List operation, returns all customers from the second function"
        }

    return response
