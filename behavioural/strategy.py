"""Strategy allows you to define a family of algorithms, put each of them in a
class, and make any instances of the classes in this family interchangeable.
"""

from abc import ABC, abstractmethod
from typing import NamedTuple, List


class Point(NamedTuple):
    x: float
    y: float


class AbstractRoutingStrategy(ABC):
    @abstractmethod
    def route(self, start: Point, end: Point) -> List[Point]:
        raise NotImplementedError()


class StraightRoutingStrategy(AbstractRoutingStrategy):
    """Routes between points in a straight line"""

    def route(self, start: Point, end: Point) -> List[Point]:
        num_points = 3
        results = []
        for i in range(num_points + 1):
            x = start.x + (end.x - start.x) * (i / num_points)
            y = start.y + (end.y - start.y) * (i / num_points)
            results.append(Point(x, y))

        return results


class UpThenAcrossRoutingStrategy(AbstractRoutingStrategy):
    """Routes between points by going up, then across"""

    def route(self, start: Point, end: Point) -> List[Point]:
        return [Point(start.x, start.y), Point(start.x, end.y), Point(end.x, end.y)]


class AcrossThenUpRoutingStrategy(AbstractRoutingStrategy):
    """Routes between points by going across, then up"""

    def route(self, start: Point, end: Point) -> List[Point]:
        return [Point(start.x, start.y), Point(end.x, start.y), Point(end.x, end.y)]


class RoutingContext:
    def __init__(self, strategy: AbstractRoutingStrategy) -> None:
        self.set_routing_strategy(strategy)

    def set_routing_strategy(self, strategy: AbstractRoutingStrategy) -> None:
        self._strategy = strategy

    def print_route(self, start: Point, end: Point):
        route = self._strategy.route(start, end)

        print(f"To get from {start} to {end}, take the following directions:")
        for point in route:
            print(point)


if __name__ == "__main__":
    start = Point(2.0, 3.0)
    end = Point(5.0, 6.0)

    ctx = RoutingContext(StraightRoutingStrategy())
    ctx.print_route(start, end)

    ctx.set_routing_strategy(UpThenAcrossRoutingStrategy())
    ctx.print_route(start, end)