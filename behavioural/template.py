"""Defines the skeleton of the algorithm in the superclass but lets subclasses
override specific steps of the algorithm without changing it's structure"""

from abc import ABC, abstractmethod
from typing import Any, Iterable


class ModelTrainer(ABC):
    def __init__(
        self,
        training_data: Iterable,
        validation_data: Iterable,
        test_data: Iterable,
        validation_labels: Iterable,
        test_labels: Iterable,
        model: Any,
    ):
        self.training_data = training_data
        self.validation_data = validation_data
        self.validation_labels = validation_labels
        self.test_data = test_data
        self.test_labels = test_labels
        self.model = model

    def train(self):
        for i in range(10):
            self.do_training_iteration(self.training_data, self.model)
            print(
                f"Validation metrics after epoch {i}:\n{self.calculate_metrics(self.validation_data, self.validation_labels, self.model)}"
            )
        print(
            f"Test metrics:\n{self.calculate_metrics(self.test_data, self.test_labels, self.model)}"
        )

    @abstractmethod
    def do_training_iteration(self, data: Iterable, model: Any):
        raise NotImplementedError()

    @abstractmethod
    def calculate_metrics(self, data: Iterable, labels: Iterable, model: Any):
        raise NotImplementedError()


class MyCustomModelTrainer(ModelTrainer):
    """We don't need to reimplement all of the mechanical model training bits in this
    class, because they are implemented in the ModelTrainer class"""
    
    def __init__(self, data: Iterable, labels: Iterable):
        model = "Initialise a model here"

        # can define my test/train/val split here
        data = list(data)
        labels = list(labels)
        super().__init__(
            training_data=data[:100],
            validation_data=data[100:150],
            test_data=data[150:200],
            validation_labels=labels[100:150],
            test_labels=labels[150:200],
            model=model,
        )

    def do_training_iteration(self, data: Iterable, model: Any):
        for row in data:
            # do some training operation on the model
            pass

    def calculate_metrics(self, data: Iterable, labels: Iterable, model: Any):
        for row, label in zip(data, labels):
            # get a result from the model
            if model(row) == label:
                pass