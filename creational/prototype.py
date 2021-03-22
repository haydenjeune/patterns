"""
The Prototype patterns allows you to copy a class without becoming dependent on it
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Shape(ABC):
    x: int = 0
    y: int = 0
    colour: str = ""

    @abstractmethod
    def _from(self, shape: Shape):
        self.x = shape.x
        self.y = shape.y
        self.colour = shape.colour

    @abstractmethod
    def clone(self) -> Shape:
        pass


@dataclass
class Rectangle(Shape):
    width: int = 0
    height: int = 0

    def _from(self, rect: Rectangle):
        super()._from(rect)
        self.width = rect.width
        self.height = rect.width

    def clone(self) -> Rectangle:
        rect = Rectangle()
        rect._from(self)
        return rect


@dataclass
class Circle(Shape):
    radius: int = 0

    def _from(self, circle: Circle):
        super()._from(circle)
        self.radius = circle.radius

    def clone(self) -> Circle:
        circle = Circle()
        circle._from(self)
        return circle


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(x=3, y=4, radius=2),
        Rectangle(x=1, y=0, width=10, height=2),
        Rectangle(x=4, y=6, width=1, height=3),
        Circle(x=3, y=4, radius=2, colour="red"),
        Rectangle(x=1, y=0, width=10, height=2),
        Circle(x=3, y=4, radius=2),
    ]

    # ok this is a little redundant without static typing, but tada!
    # we don't need to know what shapes they are exactly to make a new
    # list, just that they are shapes! Thus, this line avoid dependencies
    # on any concrete classes.
    other_shapes: List[Shape] = [s.clone() for s in shapes]