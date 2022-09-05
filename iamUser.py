from pprint import pprint
import boto3 

# using the default profile
# iam = boto3.client('iam')
# response  = iam.get_user()
# pprint(response)











# using name profiles, the session Object -  Recommended
session = boto3.Session(
    profile_name= 'gerald.njoku',
    region_name= "eu-central-1"
)
iam = session.client("iam")
response = iam.get_user()
print(f"user {response['User']['UserName']}, {response['User']['UserId']}: Created on {response['User']['CreateDate']}")









# remember the remaining configuration