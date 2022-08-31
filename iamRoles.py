import json, boto3
from pprint import pprint

# the policy
ec2_assume_role_policy_doc = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
})

# print(ec2_assume_role_policy_doc)

gerald = boto3.Session(
    profile_name= 'gerald.njoku',
    region_name= "eu-central-1"
)

# add a a new client
geraldIAM = gerald.client("iam")

# we create the role with the new client
response = geraldIAM.create_role(
    RoleName = "ec2-readonly2",
    AssumeRolePolicyDocument = ec2_assume_role_policy_doc,
    Description = "Allows am instance to ec2 read-only access",
    Tags = [
        {
            "Key": "gerald.njoku",
            "Value": "For automation with python"
        }
    ]
)

pprint(response)

# to confirm
ec2_readonly_role_name = response['Role']['RoleName']
# print(ec2_readonly_role_name)


# we create the corresponding instance profile
response = geraldIAM.create_instance_profile(
    InstanceProfileName   = ec2_readonly_role_name,
    Tags = [
        {
            "key": "gerald.njoku",
            "Value": "For automation with python"
        }
    ]
)
pprint(response)