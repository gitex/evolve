from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValueObject:
    ...


@dataclass(frozen=True)
class InRange(ValueObject):
    min: Any
    max: Any

    def __contains__(self, value: float):
        return self.min >= value <= self.max

    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            raise TypeError(f'Must be {self.__class__.__name__} type')

        return other.min == self.min and other.max == self.max


@dataclass(frozen=True)
class InFloatRange(InRange):
    min: float
    max: float


class Weight(InFloatRange):
    ...


class Health(InFloatRange):
    ...
