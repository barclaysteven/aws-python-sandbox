import boto3
import time
import re

session = boto3.Session(profile_name="vpc-design-fh4", region_name="us-east-1")
cfn_client = session.client("cloudformation")

status_filters = [
    'UPDATE_ROLLBACK_COMPLETE',
    'UPDATE_COMPLETE',
    'CREATE_COMPLETE'
]

list_stacks_response = cfn_client.list_stacks(StackStatusFilter=status_filters)

while True:
    for stack in list_stacks_response['StackSummaries']:
        stack_name = stack['StackName']
        print("Found stack: " + stack_name + ". Getting Resources.")
        stack_resources = cfn_client.describe_stack_resources(StackName=stack_name)
        for resource in stack_resources['StackResources']:
            logical_id = resource['LogicalResourceId']
            resource_type = resource['ResourceType']
            print("\t" + logical_id + " of type: " + resource_type)

    if "NextToken" in list_stacks_response.keys():
        list_stacks_response = cfn_client.list_stacks(NextToken=list_stacks_response['NextToken'],
                                                      StackStatusFilter=status_filters)
    else:
        break
