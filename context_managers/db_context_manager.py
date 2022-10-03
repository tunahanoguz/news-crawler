import psycopg2
from configs import ConfigFileParser
from exceptions import DbConnectionException


class DbContextManager(object):
    def __enter__(self):
        try:
            config_parser = ConfigFileParser('database_config.ini', 'postgresql')
            db_config = config_parser.parse()
            self.conn = psycopg2.connect(**db_config)
        except Exception:
            raise DbConnectionException
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.conn.commit()
            self.conn.close()
        except Exception:
            raise DbConnectionException
