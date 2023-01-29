from animals import Animal, AnimalGender, AnimalType
from randomizer import randomize
from typing import Callable
from functools import cached_property
from structs import Health, Weight


class AnimalFactory:
    type: AnimalType

    @cached_property
    def gender(self) -> AnimalGender:
        return randomize.from_enum(AnimalGender)

    def get_health(self) -> Health:
        raise NotImplementedError

    def get_weight(self) -> Weight:
        raise NotImplementedError

    def make(self, parent: Animal | None) -> Animal:
        return Animal(
            parent=parent,
            type=self.type,
            gender=self.gender,
            health=self.get_health(),
            weight=self.get_weight()  # TODO: make weight by gender
        )


class BuffaloFactory(AnimalFactory):
    type = AnimalType.HERBIVORE

    def get_health(self) -> Health:
        return Health(1000)  # TODO: Remove hardcode

    def get_weight(self) -> Weight:
        return randomize.from_dispersion(400, 100)


class LionFactory(AnimalFactory):
    type = AnimalType.CARNIVOROUS

    def get_health(self) -> Health:
        return Health(1000)  # TODO: Remove hardcode

    def get_weight(self) -> Weight:
        return randomize.from_dispersion(100, 50)
