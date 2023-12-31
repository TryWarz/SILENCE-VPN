import pymysql
from src.config import ConfigurationDb

db = ConfigurationDb()

class MySQL:
    def __init__(self):
        self.db_name = db.db
        self.db_host = db.host
        self.db_password = db.password
        self.db_user = db.user

    def connect(self):
        return pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name
        )
    
    def execute(self, query, params=None):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
    
    def execute_one(self, query, params=None):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
    
    def execute_insert(self, query, params=None):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
    
    def execute_update(self, query, params=None):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
            
    def execute_delete(self, query, params=None):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount

    def fetchall(self):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                return cursor.fetchall()
            
    def close(self):
        self.connect().close()
    
            
            

