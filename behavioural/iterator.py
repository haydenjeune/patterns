"""
Iterator is a behavioral design pattern that lets you traverse elements of a
collection without exposing its underlying representation
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class BinaryTree:
    value: int
    left: Optional[BinaryTree] = None
    right: Optional[BinaryTree] = None

    def breadth_first(self):
        return BreadthFirstIterator(self)

    def depth_first(self):
        return DepthFirstIterator(self)


class BreadthFirstIterator:
    def __init__(self, tree: BinaryTree):
        self.queue = [tree]

    def __iter__(self):
        # allows direct usage
        return self

    def __next__(self):
        if len(self.queue) == 0:
            raise StopIteration()

        next = self.queue.pop(0)

        if next.left is not None:
            self.queue.append(next.left)
        if next.right is not None:
            self.queue.append(next.right)

        return next


class DepthFirstIterator:
    def __init__(self, tree: BinaryTree):
        self.queue = [tree]

    def __iter__(self):
        # allows direct usage
        return self

    def __next__(self):
        if len(self.queue) == 0:
            raise StopIteration()

        next = self.queue.pop()

        if next.right is not None:
            self.queue.append(next.right)
        if next.left is not None:
            self.queue.append(next.left)

        return next


if __name__ == "__main__":
    tree = BinaryTree(
        value=10,
        left=BinaryTree(
            value=5,
            left=BinaryTree(value=2),
            right=BinaryTree(value=5, left=BinaryTree(value=3)),
        ),
        right=BinaryTree(value=2, right=BinaryTree(value=6)),
    )

    print("Breadth First Traversal")
    for node in tree.breadth_first():
        print(node.value)

    print("Depth First Traversal")
    for node in tree.depth_first():
        print(node.value)