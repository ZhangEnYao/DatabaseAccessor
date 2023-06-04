from .database_object.table import Table



def get_database_management_object(
    host,
    port,
    database,
    user,
    password,
    schema,
    table
):
    table_access_object = Table(
        host = host,
        port = port,
        database = database,
        user = user,
        password = password,
        schema = schema,
        table = table
    )
    return table_access_object