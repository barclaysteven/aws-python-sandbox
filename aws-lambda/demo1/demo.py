import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


def handler(event, context):
    ssm_client = boto3.client('ssm')

    results = ssm_client.list_documents(
        DocumentFilterList=[
            {
                "key": 'Name',
                "value": 'adhoc-p1-barclays-lambda-training'
            }
        ]
    )

    print("Document Name: {}".format(results['DocumentIdentifiers'][0]['Name']))
    print("Document Type: {}".format(results['DocumentIdentifiers'][0]['DocumentType']))
