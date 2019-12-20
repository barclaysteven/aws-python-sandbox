import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch


def create_client():
    patch(['boto3'])
    ssm_client = boto3.client('ssm')
    return ssm_client


def get_docs(client):
    response = client.list_documents(
        DocumentFilterList=[
            {
                "key": 'Name',
                "value": 'adhoc-p1-barclays-lambda-training'
            }
        ]
    )

    return response


def handler(event, context):
    print("Document Name: {}".format(results['DocumentIdentifiers'][0]['Name']))
    print("Document Type: {}".format(results['DocumentIdentifiers'][0]['DocumentType']))


client = create_client()
results = get_docs(client)
