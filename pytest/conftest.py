import pytest
from .human import Human


@pytest.fixture
def create_human():
    human = Human('Oleksandra', 29, 'female')
    yield human


@pytest.fixture()
def create_old_male_human():
    human = Human('John', 75, 'male')
    yield human


@pytest.fixture()
def create_old_female_human():
    human = Human('Sarah', 80, 'female')
    yield human


@pytest.fixture()
def create_dead_human():
    human = Human('Rick', 101, 'male')
    yield human
