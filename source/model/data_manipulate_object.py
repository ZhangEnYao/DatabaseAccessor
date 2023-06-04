from psycopg2 import extras
from .database_object.connection import Connection



class PostgresDataManipulateObect(Connection):
    
    def create(
        self,
        schema,
        table,
        data,
        target_columns
    ):
        with self.connection.cursor() as cursor:
            query = f'insert into {schema}.{table} {target_columns} values {data}'
            cursor.execute(query)
        self.connection.commit()
    
    def copy(
        self,
        schema,
        table,
        file
    ):
        with self.connection.cursor() as cursor:
            target_columns = (', ').join(file.columns)
            instances = tuple(tuple(instance) for index, instance in file.iterrows())
            query = f'insert into {schema}.{table} ({target_columns}) values %s'
            extras.execute_values(cursor, query, instances)
        self.connection.commit()
    
    def delete(
        self,
        schema,
        table,
        constraint
    ):
        query = f'delete from {schema}.{table} where {constraint}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()

    def update(
        self,
        schema,
        table,
        modification,
        constraint
    ):
        query = f'update {schema}.{table} set {modification} where {constraint}'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()