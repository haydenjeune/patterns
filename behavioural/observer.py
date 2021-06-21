"""The observer pattern is basically a pub-sub queue for classes, except the 
actual 1->n message pushing occurs in the publisher"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class Subscriber(ABC):
    @abstractmethod
    def update(self, context: Dict[str, Any]):
        raise NotImplementedError()


class PrintMessageToStdOut(Subscriber):
    def update(self, context: Dict[str, Any]):
        print(context)


class Publisher:
    def __init__(self):
        self._subscribers = set()

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        try:
            self._subscribers.remove(subscriber)
        except KeyError:
            pass

    def notify_subscribers(self, context: Dict[str, Any]):
        for subscriber in self._subscribers:
            subscriber.update(context)


class Newsletter(Publisher):
    def __init__(self, title: str, body: str):
        super().__init__()
        self.title = title
        self.body = body

    def send_to_all(self):
        self.notify_subscribers(
            {"event": "new newsletter", "title": self.title, "body": self.body}
        )


if __name__ == "__main__":
    printer_one = PrintMessageToStdOut()
    printer_two = PrintMessageToStdOut()

    newsletter = Newsletter(
        "An Announcement!", "Everyone will receive this very important announcement"
    )

    newsletter.subscribe(printer_one)
    newsletter.subscribe(printer_two)

    newsletter.send_to_all()
