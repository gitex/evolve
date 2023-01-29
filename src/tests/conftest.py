import pytest

from factories import BuffaloFactory, LionFactory


@pytest.fixture(scope='session')
def buffalo_factory() -> BuffaloFactory:
    return BuffaloFactory()


@pytest.fixture(scope='session')
def lion_factory() -> LionFactory:
    return LionFactory()
