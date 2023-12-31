from src.db import MySQL 
import unittest

mysql = MySQL() 

class DatabaseConnectionTest(unittest.TestCase):
    def __init__(self) -> None:
        self.fail = False

    def main(self):
        try:
             # Create an instance of the MySQL class
            assert mysql.connect() is not None
        except AssertionError:
            self.fail('Connection to database failed.')
        try:
            assert mysql.execute() is not None
        except AssertionError:
            self.fail('Cursor to database failed.')
        finally:
            mysql.close()
            return self.fail
