import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch


def create_client():

    patch(['boto3'])
    ssm_client = boto3.client('ssm')

    response = ssm_client.list_documents(
        DocumentFilterList=[
            {
                "key": 'Name',
                "value": 'adhoc-p1-barclays-lambda-training'
            }
        ]
    )

    return response


def get_documents():
    return create_client()
