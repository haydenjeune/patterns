"""
A substitute object with the same interface that allows you to perform things
before or after the request gets through to the original object.
"""

from typing import Protocol


class Database(Protocol):
    def get(self, id: str, key: str):
        raise NotImplementedError()


class RealDatabase:
    def get(self, id: str, key: str):
        return "the_real_data"


class AccessProxyDatabase:
    def __init__(self):
        self.db = RealDatabase()

    def get(self, id: str, key: str):
        # access control
        if id != "the right user":
            raise Exception

        return self.db.get(id, key)


class LazyInitProxyDatabase:
    def __init__(self):
        self.db = None

    def get(self, id: str, key: str):
        # lazy initialisation
        if self.db is None:
            self.db = RealDatabase()

        return self.db.get(id, key)