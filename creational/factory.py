"""
The factory pattern involves instantiating new instances of an object via a "factory" class.

At the highest level, the Factory is an interface that implements a `create` method.
The create method returns some object that implements a common interface across all types
of objects you want to create. Each type of object has it's own factory class. This Factory
class implements a create method that returns a particular type of object. You can then write
code that uses a Factory class to create concrete objects, without having to care about
exactly which type of object you have.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Model(ABC):
    @abstractmethod
    def predict(self, input):
        pass


@dataclass
class RandomGuessModel(Model):
    def predict(self, input):
        return "A random guess prediction"


@dataclass
class XGBoostModel(Model):
    param: str = "Some runtime configuration"

    def predict(self, input):
        return "An XGBoost prediction"


@dataclass
class DeepLearningModel(Model):
    model: bytes = "The binary model to execute".encode()

    def predict(self, input):
        return "A Deep Learning prediction"


class ModelFactory(ABC):
    @abstractmethod
    def create(self) -> Model:
        pass


class RandomGuessModelFactory(ModelFactory):
    def create(self) -> RandomGuessModel:
        return RandomGuessModel()


class XGBoostModelFactory(ModelFactory):
    def create(self) -> XGBoostModel:
        return XGBoostModel("configuration")


class DeepLearningModelFactory(ModelFactory):
    def create(self) -> DeepLearningModel:
        return DeepLearningModel("modeldata".encode())


if __name__ == "__main__":
    pass
