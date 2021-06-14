"""
Command turns a request into a stand-alone object that contains all information
about the request. This lets you paramaterise methods with different requests,
delay or queue a requests execution, and support undoable operations
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Stock:
    ticker: str
    quantity: int

    def buy(self):
        print(f"Bought {self.quantity} of {self.ticker}")

    def sell(self):
        print(f"Sold {self.quantity} of {self.ticker}")


class Order(ABC):
    def __init__(self, stock: Stock):
        self.stock = stock

    @abstractmethod
    def execute(self):
        pass


class BuyOrder(Order):
    def execute(self):
        self.stock.buy()


class SellOrder(Order):
    def execute(self):
        self.stock.sell()


class Broker:
    def __init__(self):
        self.orders = []

    def place_order(self, order: Order):
        self.orders.append(order)

    def execute(self):
        for order in self.orders:
            order.execute()


if __name__ == "__main__":
    buy = BuyOrder(Stock("XRO", 100))
    sell = SellOrder(Stock("XRO", 10))

    broker = Broker()

    broker.place_order(buy)
    broker.place_order(sell)
    broker.execute()