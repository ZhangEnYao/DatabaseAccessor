from ..data_query_object import PostgresDataQueryObject
from ..data_manipulate_object import PostgresDataManipulateObect



class Table(PostgresDataQueryObject, PostgresDataManipulateObect):
    def __init__(
        self,
        host,
        port,
        database,
        user,
        password,
        schema,
        table
    ):
        super(Table, self).__init__(
            host,
            port,
            database,
            user,
            password
        )
        self._schema = schema
        self._table = table
    
    @property
    def schema(self):
        return self._schema
    
    @property
    def table(self):
        return self._table
    
    @property
    def dataset(self):
        return self.read(f'select * from {self.schema}.{self.table}')
    
    @property
    def columns(self):
        column_information = self.read(f"select column_name from information_schema.columns where table_schema = '{self.schema}' and table_name = '{self.table}';")
        return (', ').join(column_information['column_name'].to_list())

    @property
    def necessary_columns(self):
        column_information = self.read(f"select column_name from information_schema.columns where table_schema = '{self.schema}' and table_name = '{self.table}'  and column_default is null;")
        return (', ').join(column_information['column_name'].to_list())