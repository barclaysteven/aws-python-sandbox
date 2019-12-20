import boto3
import time
import re

session = boto3.Session(profile_name="vpc-design-fh4", region_name="us-east-1")
cfn_client = session.client("cloudformation")

list_stacks_response = cfn_client.list_stacks()

while True:
    for stack in list_stacks_response['StackSummaries']:
        stack_name = stack['StackName']
        status = stack['StackStatus']
        print("Found stack: " + stack_name)
        print("StackStatus: " + status)
        if 'DELETE' in status or 'REVIEW' in status or 'ROLLBACK' in status:
            print("Skipping drift detection")
        else:
            print("Detecting drift for " + stack_name)
            detect_drift_response = cfn_client.detect_stack_drift(StackName=stack_name)
    if "NextToken" in list_stacks_response.keys():
        list_stacks_response = cfn_client.list_stacks(NextToken=list_stacks_response['NextToken'])
    else:
        break
