#AWS to AZURE connections
#===========================================================================#
# import psycopg2
# from psycopg2 import OperationalError

# def create_connection(db_name, db_user, db_password, db_host, db_port):
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print("Connection to PostgreSQL DB successful")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection
#===========================================================================#
from sqlite3 import connect
import psycopg2
from psycopg2 import OperationalError
from dotenv import dotenv_values

config = dotenv_values(".env")

DB_NAME = config["DB_NAME"]
DB_USER = config["DB_USER"]
DB_PW = config["DB_PW"]
DB_HOST = config["DB_HOST"]
DB_PORT = config["DB_PORT"]

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None;
    try:
        connection = psycopg2.connect(
            database = db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            sslmode = "require"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as err:
        print(f"The error '{err}' occured")
    return connection


# Create connection to PostgreSQL database (on Azure)
connection = create_connection(DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT)
