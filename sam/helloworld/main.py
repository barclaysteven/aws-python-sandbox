print('Loading function')


def handler(event, context):
    print("Value1 = " + event['key1'])
    print("Value2 = " + event['key2'])
    print("Value3 = " + event['key3'])

    return 'Hello World'
