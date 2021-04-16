"""
Lets you compose objects into tree structures and then work with these
structures as if they were individual objects.
"""

from typing import Protocol, Set


class Shippable(Protocol):
    def get_weight(self) -> float:
        raise NotImplementedError()


# This is a composite class
class Box:
    def __init__(self, items: Set[Shippable] = set()):
        self.items = items

    def add(self, item: Shippable):
        self.items.add(item)

    def remove(self, item: Shippable):
        if item in self.items:
            self.items.remove(item)

    # Implements Shippable protocol
    def get_weight(self) -> float:
        return sum([item.get_weight() for item in self.items])


class KakapoFeather:
    def get_weight(self) -> float:
        return 0.01


class SomethingSquashable:
    def get_weight(self) -> float:
        return 0.1


class Dumbell:
    def get_weight(self) -> float:
        return 8.0


class Book:
    def get_weight(self) -> float:
        return 2


class Compass:
    def get_weight(self) -> float:
        return 0.3


class LimitedEditionLukeSkywalkerFigurine:
    def get_weight(self) -> float:
        return 0.5


if __name__ == "__main__":
    # put the precious things in one box
    precious_box = Box(
        {
            KakapoFeather(),
            LimitedEditionLukeSkywalkerFigurine(),
            SomethingSquashable(),
            SomethingSquashable(),
        }
    )

    print(f"There's {precious_box.get_weight()}kgs of precious goods")

    # chuck everything else in one big box for shipping
    main_box = Box(
        {
            precious_box,
            Book(),
            Dumbell(),
            Compass(),
        }
    )

    print(f"The whole shipment weighs {main_box.get_weight()}kgs ")
