import pytest

from pytest.human import Human


def test_gender_type(create_human):
    # Test that Gender should be string value
    human = create_human
    result = human.gender
    assert isinstance(result, str), 'Gender should be string value'


def test_age_type(create_human):
    # Test that Age should be int value
    human = create_human
    result = human.age
    assert isinstance(result, int), 'Age should be int value'


def test_grow(create_human):
    # Test that Age should be grown
    human = create_human
    new_age = human.age + 1
    human.grow()
    assert human.age == new_age


def test_change_gender_to_male(create_human):
    # Test that Gender should be changed
    human = create_human
    human.change_gender("male")
    assert human.gender == "male"


def test_age_limit_exceeded(create_human):
    # Test that age does not increase after exceeding the age limit
    create_human._Human__age = 100
    create_human.grow()
    assert create_human.age == 100


def test_multiple_grow(create_human):
    # Test that the age increases correctly with multiple calls to grow()
    create_human.grow()
    create_human.grow()
    create_human.grow()
    assert create_human.age == 32


def test_is_alive_after_grow(create_human):
    # Test that the human is alive after growing
    create_human.grow()
    assert create_human._Human__is_alive()


def test_change_gender_multiple_times(create_human):
    # Test that gender can be changed multiple times and remains correct
    create_human.change_gender("female")
    create_human.change_gender("male")
    assert create_human.gender == "male"


def test_change_gender_and_age(create_human):
    # Test that changing gender does not affect the age
    create_human.change_gender("male")
    create_human.grow()
    assert create_human.age == 29


def test_change_gender_when_dead(create_human):
    # Test attempting to change gender after the human is dead
    create_human._Human__age = 105
    with pytest.raises(Exception):
        create_human.change_gender("male")
