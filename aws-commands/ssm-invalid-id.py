import boto3

aws_session = boto3.Session(profile_name="play-fh2")

ssm_client = aws_session.client("ssm")

target = {
    'Key': 'instanceids',
    'Values': [
        'i-0b739f051e56a01d0'
    ]
}

parameters = {
    'Message': [
        "Hello"
    ]
}

response = ssm_client.send_command(Targets=[target],
                                   DocumentName='adhoc-p1-barclays-lambda-training',
                                   Parameters=parameters,
                                   TimeoutSeconds=30
                                   )
