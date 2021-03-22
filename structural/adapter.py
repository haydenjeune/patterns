"""
Adapter is a structural design pattern that allows objects with
incompatible interfaces to collaborate.
"""

from dataclasses import dataclass

@dataclass
class SquarePeg():
    width: float

@dataclass
class RoundPeg():
    radius: float

@dataclass
class RoundHole():
    radius: float
    
    def fits(self, peg: RoundPeg) -> bool:
        return peg.radius <= self.radius

class SquarePegAdapter(RoundPeg):
    """
    Must implement the RoundPeg interface, in another language we'd lock this down
    """
    def __init__(self, peg: SquarePeg):
        self.peg = peg

    @property
    def radius(self) -> float:
        return self.peg.width/2

if __name__ == "__main__":
    hole = RoundHole(1)
    round_peg = RoundPeg(1)
    square_peg = SquarePeg(2)
    big_square_peg = SquarePeg(3)

    square_peg_adapter = SquarePegAdapter(square_peg)
    big_square_peg_adapter = SquarePegAdapter(big_square_peg)

    print(hole.fits(round_peg))
    print(hole.fits(square_peg_adapter))
    print(hole.fits(big_square_peg_adapter))