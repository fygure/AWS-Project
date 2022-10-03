import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
#===========================================================================#
# Create IAM User
def create_iam_user(user_name):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.create_user(UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return response
# TEST CODE IN SERVER
# responseObject = iam_functions.create_iam_user("Test1")
# print(responseObject)
#===========================================================================#
# List all IAM users
def list_iam_users():
    try:
        iam_client = boto3.client('iam')
        paginator = iam_client.get_paginator('list_users')
        for response in paginator.paginate():
            for user in response["Users"]:
                print("Username: ", user["UserName"])
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
#list_iam_users()
#===========================================================================#
# Update an IAM username
def update_iam_user(existing_username, new_username):
    try:
        iam_client = boto3.client('iam')
        iam_client.update_user(UserName=existing_username, NewUserName=new_username)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")

#update_iam_user("Test1, "Test2")
#===========================================================================#
# Delete an IAM user
def delete_iam_user(existing_username):
    try:
        iam_client = boto3.client('iam')
        iam_client.delete_user(UserName=existing_username)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")

#delete_iam_user("Test2")
#===========================================================================#