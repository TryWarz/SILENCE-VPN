from src.db import MySQL 
import unittest


class DatabaseConnectionTest(unittest.TestCase):
    def __init__(self) -> None:
        self.fail = False

    def main(self):
        try:
            assert MySQL.connect() is not None
        except AssertionError:
            self.fail('Connection to database failed.')
        try:
            assert MySQL.execute() is not None
        except AssertionError:
            self.fail('Cursor to database failed.')
        finally:
            MySQL.close()
            return self.fail
