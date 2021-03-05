"""
The abstract factory pattern is like the factory pattern, but with an extra layer of indirection.

Instead of just having a single create method, each factory implements a set of different
create methods, one for each category (where category is like a different type, but in different
dimension).

For example, the factory pattern could be used where FurnitureFactory can create tables, chairs, 
and stools. The abstract factory pattern would involve extending this so that different
categories of tables, chairs, and stools can be created (eg victorian chairs, modern chairs, etc.)
So, the FurnitureFactory could be extended into a VictorianFactory, and ModernFactory. Each of
which would implement createChair, createTable, and createStool. This would allow the caller
to create a set of furniture with consistent style, without having to know which style that is.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Chair(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass


@dataclass
class Table(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def weight_rating(self) -> int:
        pass


@dataclass
class Stool(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def leg_count(self) -> int:
        pass


class Factory(ABC):
    @abstractmethod
    def createChair(self) -> Chair:
        pass

    @abstractmethod
    def createTable(self) -> Table:
        pass

    @abstractmethod
    def createStool(self) -> Stool:
        pass


class FancyChair(Chair):
    def describe(self) -> str:
        return "There are four legs made of a very aesthetically pleasing material."


class FancyTable(Table):
    def describe(self) -> str:
        return "The table is perfectly smooth and cool to the touch. It feels sturdy and well-built."

    def weight_rating(self) -> int:
        return 1000  # (kgs)


class FancyStool(Stool):
    def describe(self) -> str:
        return "The stool is the perfect hight to sit at. Despite the lack of padding, it is very comfortable."

    def leg_count(self) -> int:
        return 4


class FancyFactory(Factory):
    def createChair(self) -> Chair:
        return FancyChair()

    def createTable(self) -> Table:
        return FancyTable()

    def createStool(self) -> Stool:
        return FancyStool()


class RicketyChair(Chair):
    def describe(self) -> str:
        return "The chair is rough, worn, and creaks as you sit in it."


class RicketyTable(Table):
    def describe(self) -> str:
        return "The table is covered in water stains, and has a nasty habit of leaving splinters in your hands."

    def weight_rating(self) -> int:
        return 20  # (kgs)


class RicketyStool(Stool):
    def describe(self) -> str:
        return "The stool cannot stand upright owing to it's missing leg."

    def leg_count(self) -> int:
        return 2


class RicketyFactory(Factory):
    def createChair(self) -> Chair:
        return RicketyChair()

    def createTable(self) -> Table:
        return RicketyTable()

    def createStool(self) -> Stool:
        return RicketyStool()


def create_scene(factory: Factory):
    chair = factory.createChair()
    table = factory.createTable()
    stool = factory.createStool()

    print("Chair description:")
    print(chair.describe())

    print(
        f"The table can take {table.weight_rating()} kgs of weight, and the stool has {stool.leg_count()} legs"
    )


if __name__ == "__main__":
    print("\n\nRunning fancy create_scene:\n\n")
    create_scene(FancyFactory())

    print("\n\nRunning rickety create_scene:\n\n")
    create_scene(RicketyFactory())