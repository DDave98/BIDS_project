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
    def insert_data(client,table,data):
        values_str = ','.join(f"'{v}'" if not isinstance(v, (int, float)) else str(v) for v in data)
        query = f"INSERT INTO {table} (ticker, open, close, high, low, volume, adj_price, pub_date) VALUES ({values_str})"
        print(query)
        result = client.query(query)
        return result

    #Used to query data
    def query(client, i_query):
        result = client.query(i_query)
        return result