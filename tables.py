# Project to demonstrate skills
# Maximillian Chalitsios 10/2/2022
#=========================================================================================#
"""Functions in this script will help with postgreSQL creation of tables and methods"""
#=========================================================================================#
from psycopg2 import OperationalError
#=========================================================================================#
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed sucessfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
#=========================================================================================#
# Create table
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    user_id TEXT NOT NULL,
    user_arn TEXT NOT NULL,
    date_created TEXT NOT NULL,
    user_groups TEXT
)
"""
#=========================================================================================#
# Practice - Don't Use
# Drop previous table of same name if one exists
# cursor.execute("DROP TABLE IF EXISTS inventory;")
# print("Finished dropping table (if existed)")

# Create a table
# cursor.execute("CREATE TABLE inventory ();")
# print("Finished creating table")

#=========================================================================================#
# def init_data():

#=========================================================================================#