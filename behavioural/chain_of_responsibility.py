"""
Chain of Responsibility lets you pass requests along a chain of handlers.
Each handler either handles the request, or passes it on to the next handler.

A good example of this pattern is the concept of 'Middleware' in web frameworks
such as .NET Core and FastAPI
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import partial
from typing import Any, Callable
from logging import getLogger

log = getLogger(__name__)


@dataclass
class Request:
    body: str
    path: str
    token: str


@dataclass
class Response:
    body: str
    status: int


class BaseMiddleware(ABC):
    def __init__(self, next: BaseMiddleware):
        self.next = next

    @abstractmethod
    def handle(self, request: Request) -> Response:
        pass


class LoggingMiddleware(BaseMiddleware):
    def handle(self, request: Request) -> Response:
        response = self.next.handle(request)
        log.info(f"[{response.status}] {request.path}")
        return response


class AuthenticationMiddleware(BaseMiddleware):
    def handle(self, request: Request) -> Response:
        if request.token != "valid":
            return Response(body="Unauthenticated", status=401)

        return self.next.handle(request)


class RoutingMiddleware(BaseMiddleware):
    def __init__(self):
        self.routes = {
            "ping": lambda req: Response(body="Ok", status=200),
            "sayhello": lambda req: Response(body="Hello", status=200),
            "echo": lambda req: Response(body=req.body, status=200),
        }

    def handle(self, request: Request) -> Response:
        if request.path not in self.routes:
            return Response(body="Not Found", status=404)

        return self.routes[request.path](request)


class Server:
    def __init__(self):
        self.request_stack = LoggingMiddleware(
            AuthenticationMiddleware(RoutingMiddleware())
        )

    def send(self, request: Request) -> Response:
        return self.request_stack.handle(request)


if __name__ == "__main__":
    s = Server()

    req = Request("Blah blah", "echo", "invalid")
    resp = s.send(req)
    print("\n")
    print(req)
    print(resp)
    print("\n")

    req = Request("Blah blah", "echo", "valid")
    resp = s.send(req)
    print(req)
    print(resp)
    print("\n")

    req = Request("", "sayhello", "valid")
    resp = s.send(req)
    print(req)
    print(resp)
    print("\n")

    req = Request("", "doesn't exist", "valid")
    resp = s.send(req)
    print(req)
    print(resp)
    print("\n")