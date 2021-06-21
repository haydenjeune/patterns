"""State lets an object alter it's behaviour when the internal state changes"""

from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, context: Dog):
        self.context = context

    @abstractmethod
    def bark(self):
        raise NotImplementedError()


class NewBorn(State):
    def bark(self):
        print("A squeak")


class Puppy(State):
    def bark(self):
        print("A high pitched yelp")


class Adult(State):
    def bark(self):
        print("A deep bark")


class Dog:
    def __init__(self):
        self.state = NewBorn(self)

    def bark(self):
        return self.state.bark()

    def change_state(self, new_state: State):
        self.state = new_state


if __name__ == "__main__":
    dog = Dog()
    dog.bark()

    dog.change_state(Puppy(dog))
    dog.bark()

    dog.change_state(Adult(dog))
    dog.bark()
