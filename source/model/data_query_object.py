from pandas import read_sql
from .database_object.connection import Connection



class PostgresDataQueryObject(Connection):
    
    def read(
        self,
        query
    ):
        return read_sql(
            sql = query,
            con = self.connection
        )