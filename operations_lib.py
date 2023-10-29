from connect_db import Client

class DefaultOperations():

    #get schema of table from @table
    def get_schema(table):
        schema = table.schema
        return schema

    #select * from table
    def get_data(client,table):
        query = f"SELECT * FROM {table}"
        result = client.query(query)
        return result

    #Do not use without sending in real data, better to use query(client, i_query)
    def insert_data(client,table):
        query = f"INSERT INTO {table} (ticker,price) VALUES ('MSFT',2000)"
        result = client.query(query)
        return result

    #Used to query data
    def query(client, i_query):
        result = client.query(i_query)
        return result
    