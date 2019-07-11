import pprint


print('Loading Function')


def handler(event, context):
    print("Event: " + str(event))
    print("Method: " + event['httpMethod'])
    print("Path: " + event['resource'])
    print("Body: " + str(event['body']))

    method = event['httpMethod']
    customer = event['pathParameters']['customer'] if event['pathParameters'] is not None else False
    if method == "GET":
        if customer:
            response = {
                "statusCode": 200,
                "body": "This is a Read operation on customer: " + customer
            }
            return response
    elif method == "POST":
        response = {
            "statusCode": 200,
            "body": "This is a Create operation."
        }
    elif method == "PUT":
        response = {
            "statusCode": 200,
            "body": "This is an Update operation on customer: " + customer
        }
    elif method == "DELETE":
        response = {
            "statusCode": 200,
            "body": "This is a Delete operation on customer: " + customer
        }
    else:
        print("Error: unsupported HTTP method: " + method)
        response = {
            "statusCode": 501,
        }

    return response
