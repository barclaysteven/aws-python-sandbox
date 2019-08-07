import json

print('Loading Function')


def handler(event, context):
    print("Event: " + str(event))
    print("Method: " + event['httpMethod'])
    print("Path: " + event['resource'])
    print("Body: " + str(event['body']))

    method = event['httpMethod']

    return_body_get = {
        "id": "1",
        "name": "Star Wars: A New Hope",
        "description": "Movie from a galaxy far far away",
        "genre": "Sci-Fi",
        "year": "1977"
    }

    if method == "GET":
        response = {
            "statusCode": 200,
            # "body": "Get operation"
            "body": json.dumps(return_body_get)
        }
    elif method == "DELETE":
        response = {
            "statusCode": 200,
            "body": "This is a DELETE operation."
        }
    elif method == "POST":
        response = {
            "statusCode": 200,
            "body": "This is a Create operation."
        }
    else:
        print("Error: unsupported HTTP method: " + method)
        response = {
            "statusCode": 501,
        }

    return response
