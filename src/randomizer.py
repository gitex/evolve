import random
import enum


class Randomize:
    def from_enum(self, choices: enum.Enum) -> enum.Enum:
        ...

    def from_dispersion(self, value: float, dispersion: float) -> float:
        ...


randomize = Randomize()
