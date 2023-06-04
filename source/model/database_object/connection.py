from logging import debug

from psycopg2 import connect



class Connection(object):

    def __init__(
        self,
        host,
        port,
        database,
        user,
        password
    ):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self.connect()
    
    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def database(self):
        return self._database

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password
    
    def connect(self):
        self.connection = connect(
            host = self.host,
            port = self.port,
            database = self.database,
            user = self.user,
            password = self.password
        )
    
    def reconnect(self):
        try:
            self.connection.close()
        except Exception as error_message:
            debug(error_message)
        finally:
            self.connection = connect(
                host = self.host,
                port = self.port,
                database = self.database,
                user = self.user,
                password = self.password
            )