"""
An optimisation that lets you fit more objects into memory by sharing common
state rather than duplicating it.
"""
from __future__ import annotations
from typing import List


class Game:
    def __init__(self, particles: List[Particle]):
        self.particles = particles or []

    def draw(self):
        for p in self.particles:
            p.draw()


class ParticleFlyweight:
    """Encapsulates intrinsic state that is duplicated between particles"""

    _singleton: ParticleFlyweight

    def __init__(self):
        self._sprite: bytes = b""
        raise NotImplementedError

    @property
    def sprite(self):
        return self._sprite

    @classmethod
    def get(cls) -> ParticleFlyweight:
        """Singleton instantiation to ensure only one copy of data exists"""
        if not getattr(cls, "_singleton", None):
            setattr(cls, "_singleton", cls())
        return cls._singleton


class BulletFlyweight(ParticleFlyweight):
    def __init__(self):
        self._sprite: bytes = b"A picture of a bullet"


class ShrapnelFlyweight(ParticleFlyweight):
    def __init__(self):
        self._sprite: bytes = b"A picture of some shrapnel"


class Particle:
    """Contains extrinsic state that is lightweight and frequently modified"""

    def __init__(self, x: int, y: int, flyweight: ParticleFlyweight):
        self.x, self.y = x, y
        self.flyweight = flyweight

    def draw(self):
        print(f"Using sprite with ID: {id(self.flyweight.sprite)}")


if __name__ == "__main__":
    particles = [
        Particle(0, 0, BulletFlyweight.get()),
        Particle(93, 5, BulletFlyweight.get()),
        Particle(2, 32, BulletFlyweight.get()),
        Particle(1, 7, ShrapnelFlyweight.get()),
        Particle(2, 7, ShrapnelFlyweight.get()),
        Particle(3, 7, ShrapnelFlyweight.get()),
    ]

    game = Game(particles)
    game.draw()
    print("See, now we only need to use 1 copy of each sprites intrinsic data")
