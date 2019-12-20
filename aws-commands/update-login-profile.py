import boto3
import pprint

aws_session = boto3.Session(profile_name="jump-sts")

iam_client = aws_session.client("iam")

pp = pprint.PrettyPrinter(indent=2)

result = iam_client.update_login_profile(UserName="barclays",
                                         Password="ChangeM3!",
                                         PasswordResetRequired=True)

pp.pprint(result)
