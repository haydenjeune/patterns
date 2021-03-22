"""
Singleton is a design pattern that lets you ensure that a class has only one instance,
while providing a global access point to this instance.
"""
from __future__ import annotations
from typing import Optional


class Database:
    # NOT a dataclass in this case, it's a class attribute
    _instance: Optional[Database] = None

    def __new__(cls) -> Database:
        if not isinstance(cls._instance, cls):
            print("This only happens once!")
            # need to aquire lock here for thread safety
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    db3 = Database()

    print(f"ID of db1: {id(db1)}")
    print(f"ID of db2: {id(db2)}")
    print(f"ID of db3: {id(db3)}")

    assert id(db1) == id(db2)
    assert id(db1) == id(db3)
