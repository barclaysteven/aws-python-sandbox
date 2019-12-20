import boto3
import pprint

session = boto3.Session(profile_name="vpc-design-fh4", region_name="us-east-1")
cfn_client = session.client("cloudformation")

pp = pprint.PrettyPrinter(indent=2)

dpt_stacks = [
    "Org-Organization-Pipeline",
    "Org-Organization-Pipeline-PreMFAPolicy",
    "Org-Organization-Pipeline-Policies",
    "Org-Organization-Pipeline-RolesAndGroups",
    "Org-Organization-Pipeline-RegionalResources",
    "Org-Organization-Pipeline-AccountResources",
    "Org-Account-Pipeline",
    "Org-Account-Pipeline-FHDCPolicies",
    "Org-Account-Pipeline-FHDCPoliciesAdhoc",
    "Org-Account-Pipeline-FHDCRolesAndGroups",
    "Account-Platform-Pipeline",
    "Org-Account-Pipeline-FHDTPolicies",
    "Org-Account-Pipeline-FHDTPolicies-StorageOperations",
    "Org-Account-Pipeline-FHDTPolicies-MgmtGovOperations",
    "Org-Account-Pipeline-FHDTPolicies-DevToolsOperations",
    "Org-Account-Pipeline-FHDTPolicies-AppIntegrationOperations",
    "Org-Account-Pipeline-FHDTPolicies-SecurityIdentOperations",
    "Org-Account-Pipeline-FHDTPolicies-NetworkingOperations",
    "Org-Account-Pipeline-FHDTPolicies-DatabaseOperations",
    "Org-Account-Pipeline-FHDTPolicies-ComputeOperations",
    "Org-Account-Pipeline-FHDTPolicies-CatchallOperations",
    "Org-Account-Pipeline-FHDTRolesAndGroups",
    "Account-Platform-Pipeline-Policies",
    "Account-Platform-Pipeline-RolesAndGroups",
    "Account-Platform-Pipeline-Users",
    "Account-Platform-Pipeline-Account-Resources",
    "Account-Platform-Pipeline-Regional-Resources",
    "PAAS-S3",
    "PAAS-resources",
    "Account-Platform-Pipeline-MainDelegation",
    "paas-pipeline-infrastructureDelegation",
    "vpc-3-2",
    "vpc-3-2-routeTables-Q0507HCBCUWN",
    "vpc-3-2-interfaces-CZEG3QWPNX4S",
    "vpc-3-2-subnets-RHSXLCCPJB1N",
    "vpc-3-2-securityGroups-CH0VZM0E07O2",
    "vpc-3-2-endpoints-1K9VNT7DSTVFK",
    "vpc-3-2-route53-1Y2JFG3Z9W7CM",
    "VPC-acl-5-primary",
    "VPC-acl-5-primary-dmzACLs-1UB39GG865TH4",
    "VPC-acl-5-primary-toolsACLs-5K5S605PDCUJ",
    "VPC-acl-5-primary-dataACLs-1IODTATF559GF",
    "VPC-acl-5-primary-privateACLs-67JQX8MBRG5D",
    "VPC-acl-5-primary-publicACLs-Z7ZZFZYHCV0E",
    "PAAS-iam-1",
    "VPC-dns-6-primary-3",
    "AccountS3",
    "VPC-vpc-aux1-1",
    "ps-temp-service-roles",
    "Account-IAM-SSHAccess-1",
    "VPC-proxy-2-primary",
    "AccountUsers",
    "AccountRoles",
    "Account-IAM-SuperAdmin-1",
    "VPC-rtg-7",
    "VPC-ssh-8-primary",
    "VPC-SecurityGroupLinks-1",
    "AccountGroups",
    "AccountInit",
    "Account-IAM-ManagedPolicies",
    "Account-IAM-ManagedPoliciesAdhoc",
    "Account-ECR-Repo-1",
    "AccountResources",
    "VPC-canonicalVips-1-primary",
    "vpc-r53-resolver"
]

file = open("/home/barclays/workspace/scratch-pad/tasks/cfn-drift-investigation.txt", "w+")

for stack in dpt_stacks:
    cnt = 1
    file.write(stack + "\n")
    stack_resources = cfn_client.describe_stack_resources(StackName=stack)
    file.write("Number of resources: " + str(len(stack_resources['StackResources'])) + "\n")
    for resource in stack_resources['StackResources']:
        file.write("\t" + str(cnt) + ". Logical Id: " + resource['LogicalResourceId'] +
                   " Resource Type: " + resource['ResourceType'] + "\n")
        cnt += 1
    file.write("\n")

file.close()






