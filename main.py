# Project to demonstrate skills
# Maximillian Chalitsios 10/2/2022
# MAIN
#===========================================================================#
import iam_functions
from azure import create_connection, DB_HOST, DB_NAME, DB_PORT, DB_PW, DB_USER
from tables import execute_query, create_users_table, execute_read_query
from datetime import date, datetime
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
def convert_to_tuple(listy):
    return tuple(listy)
#===========================================================================#
# JSON Serializer for objects
def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
#===========================================================================#

#===========================================================================#
# Connects to Azure PostgreSQL DB and executes query!
#conn_string = f"host={DB_HOST} user={DB_USER} dbname={DB_NAME} password={DB_PW} sslmode=require"
connection = create_connection(DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT)

# EXECUTE QUERY (DO IT ONCE)
#execute_query(connection, create_users_table)
#===========================================================================#
"""BELOW CONTAINS DATA PULLED FROM AWS IAM ACCOUNT"""
name_list = iam_functions.list_iam_users()
#print(name_list)

# UNCOMMENT TO TEST INDIVIDUAL BELOW
# user_info = iam_functions.get_user_info("MAX")
# group_info_user = iam_functions.get_user_group("MAX")
# username = user_info["User"]["UserName"]
# user_ID = user_info["User"]["UserId"]
# user_arn = user_info["User"]["Arn"]
# date_created = user_info["User"]["CreateDate"]
# user_groups = group_info_user["Groups"][0]["GroupName"]
#p1 = objects.User(username, user_ID, user_arn, date_created, user_groups)
#print(p1.user_arn)

# Parse data below to insert query
users = []

for name in name_list:
    info = iam_functions.get_user_info(name)
    groups = iam_functions.get_user_group(name)
    temp_list = []
    temp_list.append(info["User"]["UserName"])
    temp_list.append(info["User"]["UserId"])
    temp_list.append(info["User"]["Arn"])
    temp_list.append(json_serial(info["User"]["CreateDate"]))
    temp_list.append(groups["Groups"][0]["GroupName"])
    tupe = convert_to_tuple(temp_list)
    users.append(tupe)

# for i in users:
#     print(i)
#===========================================================================#
# COMMENT AFTER RUN
#user_records = ", ".join(["%s"] * len(users))
#print(user_records)
# insert_query = (
#     f"INSERT INTO employees (name, id, arn, date_created, groups) VALUES ({user_records})"
# )
# cursor = connection.cursor()
# cursor.execute(insert_query, users)
# connection.commit()
#===========================================================================#
# COMMENT AFTER RUN
# THIS DROPS THE WHOLE TABLE (DONT DO THIS LOL)
# drop_table_query = (
#     f"DROP TABLE users;"
# )
# cursor = connection.cursor()
# cursor.execute(drop_table_query)
#===========================================================================#
# COMMENT AFTER RUN
# testid = "testid2"
# delete_query = (
#     f"DELETE FROM employees WHERE id = '{str(testid)}'"
# )
# cursor = connection.cursor()
# cursor.execute(delete_query)
# connection.commit()
#===========================================================================#
# COMMENT AFTER RUN
# insert_query = (
#     f"INSERT INTO employees (name, id, arn, date_created, groups) VALUES (%s, %s, %s, %s, %s)"
# )
# cursor = connection.cursor()
# cursor.execute(insert_query, ("testname2", "testid2", "testarn2", "testdate2", "testgroup2"))
# connection.commit()
#===========================================================================#
# GRABS DATA FROM DATABASE
select_employees = "SELECT * FROM employees"
employees = execute_read_query(connection, select_employees)
print(employees)
#===========================================================================#


#===========================================================================#
#===========================================================================#
#===========================================================================#
#===========================================================================#
#===========================================================================#
connection.close()
#===========================================================================#