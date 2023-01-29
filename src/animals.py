from dataclasses import dataclass, field
from enum import Enum
import typing as t

from structs import Weight, Health


class AnimalType(Enum):
    HERBIVORE = 'Травоядное'
    CARNIVOROUS = 'Плотоядное'
    OMNIVORE = 'Всеядное'


class AnimalGender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


@dataclass
class Animal:
    parent: t.Self | None
    type: AnimalType
    gender: AnimalGender
    health: Health
    weight: Weight
