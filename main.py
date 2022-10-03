# Project to demonstrate skills
# Maximillian Chalitsios 10/2/2022
# MAIN
#===========================================================================#
import iam_functions
import objects
from azure import create_connection, DB_HOST, DB_NAME, DB_PORT, DB_PW, DB_USER, put_data
#===========================================================================#
# Run these commands once
# Create client to connect to iam services using boto3
""" Need Paginator to list users to get username to then get their access key """
# client = boto3.client('iam')
# paginator = client.get_paginator('list_users')
# for response in paginator.paginate():
#     print(response)

# responseObject = iam_functions.create_iam_user("Test1")
# print(responseObject)

# iam_functions.list_iam_users()
# iam_functions.update_iam_user("Test1", "Test2")
# iam_functions.list_iam_users()
# iam_functions.delete_iam_user("Test2")

# custom_policy_json = {
#         "Version": "2012-10-17",
#         "Statement": [{
#             "Effect": "Allow",
#             "Action": [
#                 "ec2:*"
#             ],
#             "Resource": "*"
#         }]
#     }

#iam_functions.create_iam_policy("swag", custom_policy_json)
#iam_functions.delete_iam_user("test100")
#iam_functions.attatch_custom_iam_policy_with_user("swag", "MAX")
#iam_functions.attatch_managed_iam_policy_with_user("AWSMarketplaceFullAccess", "MAX")
#iam_functions.detach_custom_policy_from_user("swag", "MAX")
#iam_functions.detach_managed_policy_from_user("AWSMarketplaceFullAccess", "MAX")
#===========================================================================#

connection = create_connection(DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT)

#===========================================================================#
"""BELOW CONTAINS DATA PULLED FROM AWS IAM ACCOUNT"""
name_list = iam_functions.list_iam_users()
#print(name_list)
user_info = iam_functions.get_user_info("MAX")
group_info_user = iam_functions.get_user_group("MAX")

username = user_info["User"]["UserName"]
user_ID = user_info["User"]["UserId"]
user_arn = user_info["User"]["Arn"]
date_created = user_info["User"]["CreateDate"]
user_groups = group_info_user["Groups"][0]["GroupName"]

p1 = objects.User(username, user_ID, user_arn, date_created, user_groups)
#print(p1.user_arn)
#===========================================================================#

put_data(p1)