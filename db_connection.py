import pyodbc
from decouple import config


def db_connect():
    server = config('DB_SERVER')
    database = config('DB_DATABASE')
    username = config('DB_USERNAME')
    password = config('DB_PASSWORD')
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    try:
        connection =pyodbc.connect(connectionString)
        print("Succesfully connected to DB")
        return connection.cursor()
    except:
        print("Cannot connect to DB")