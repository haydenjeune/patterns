"""Allows the separation of algorithms from the objects on which they operate"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class BaseNode(ABC):
    value: Any
    left: Optional[BaseNode] = None
    right: Optional[BaseNode] = None

    @abstractmethod
    def accept(self, visitor: NodeVisitor):
        raise NotImplementedError()


@dataclass
class StrNode(BaseNode):
    value: str

    def accept(self, visitor: NodeVisitor):
        visitor.visit_str(self)


@dataclass
class IntNode(BaseNode):
    value: int

    def accept(self, visitor: NodeVisitor):
        visitor.visit_int(self)


@dataclass
class FloatNode(BaseNode):
    value: float

    def accept(self, visitor: NodeVisitor):
        visitor.visit_float(self)


class NodeVisitor(ABC):
    @abstractmethod
    def visit_str(self, node: StrNode):
        raise NotImplementedError()

    @abstractmethod
    def visit_int(self, node: IntNode):
        raise NotImplementedError()

    @abstractmethod
    def visit_float(self, node: FloatNode):
        raise NotImplementedError()


# now we can add new visitor logic without changing the node classes
class BasicPrintVisitor(NodeVisitor):
    def visit_str(self, node: StrNode):
        print(f"String Node: {node.value}")

    def visit_int(self, node: IntNode):
        print(f"Int Node: {node.value}")

    def visit_float(self, node: FloatNode):
        print(f"Float Node: {node.value:.2f}")


def bfs(node: BaseNode):
    stack = [node]

    while len(stack):
        next = stack.pop(0)
        if next.left:
            stack.append(next.left)
        if next.right:
            stack.append(next.right)
        yield next


if __name__ == "__main__":
    tree = IntNode(
        value=3,
        left=StrNode(value="Hello", right=StrNode(value="there")),
        right=FloatNode(value=3.14),
    )

    visitor = BasicPrintVisitor()

    for node in bfs(tree):
        node.accept(visitor)
