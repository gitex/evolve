from animals import Animal


class Plant:
    def __init__(self, animals: list[Animal]):
        self._animals = animals

    def __iter__(self):
        return iter(self._animals)
