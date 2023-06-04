from dataclasses import dataclass



@dataclass(frozen=True)
class Configuration(object):
    host: str
    port: str
    database: str
    user: str
    password: str
    schema: str
    table: str

Configurations = {    
        'database_accessor_testing_event': Configuration(
            '127.0.0.1',
            '5432',
            'en-yao_zhang',
            'postgres',
            'password',
            'public',
            'jeff'
        )
    }