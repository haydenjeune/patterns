"""
The builder pattern utilises a builder object 
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional


class Builder(ABC):
    @abstractmethod
    def add_auth(self, token: str):
        pass

    @abstractmethod
    def add_endpoint(self, path: str, response: str):
        pass

    @abstractmethod
    def add_healthcheck(self):
        pass

    @abstractmethod
    def finalise(self) -> Any:
        pass


@dataclass
class API:
    endpoints: dict = {}
    auth_token: Optional[str] = None

    def get(self, path: str, token: str = None) -> str:
        if self.auth_token is not None and token != self.auth_token:
            return "Error: Unauthenticated"

        try:
            return self.endpoints[path]
        except KeyError as e:
            return "Error: endpoint path not found"


class APIBuilder(Builder):
    def __init__(self):
        self.api = API()

    def add_auth(self, token: str):
        self.api.auth_token = token

    def add_endpoint(self, path: str, response: str):
        self.api.endpoints[path] = response

    def add_healthcheck(self):
        self.add_endpoint("healthcheck", "OK")

    def finalise(self) -> API:
        return self.api


if __name__ == "__main__":
    builder = APIBuilder()
    builder.add_auth("fake_token")
    builder.add_endpoint("test", "this is the test endpoint")
    builder.add_healthcheck()
    api = builder.finalise()

    api.get("test", "fake_token")  # returns "this is the test endpoint"
    api.get("healthcheck", "fake_token")  # returns "OK"
