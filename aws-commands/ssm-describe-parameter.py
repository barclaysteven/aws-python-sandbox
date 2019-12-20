import boto3
import pprint

aws_session = boto3.Session(profile_name="mgmt-fh7")

ssm_client = aws_session.client("ssm")

pp = pprint.PrettyPrinter(indent=2)

result = ssm_client.describe_parameters(
    ParameterFilters=[
        {
            'Key': 'Path',
            'Option': 'OneLevel',
            'Values': ['/priv-1/target-api/account/']
        }
    ])

while 'NextToken' in result:
    print(result['NextToken'])

pp.pprint(result)
