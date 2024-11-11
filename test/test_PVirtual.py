import pytest

from pvirtual import PVirtual

@pytest.fixture
def pieza():
    return PVirtual()

def test_get_characters(pieza):
    assert pieza.get_characters() == [-100, -100, -100, -100, -100]


def test_set_characters(pieza):
    pieza.set_characters([1, 2, 3, 2, 1])
    assert  pieza.get_characters() == [1, 2, 3, 2, 1]


def test_get_character_val(pieza):
    pieza.set_characters([1, 2, 3, 2, 1])
    assert pieza.get_character_val(4) == 1


def test_set_character_val(pieza):
    pieza.set_character_val(8, 3)
    assert pieza.get_character_val(3) == 8

def test_get_status_ok(pieza):
    assert pieza.get_status_ok() == [False, False, False, False, False]


def test_set_status_ok(pieza):
    pieza.set_status_ok([True, False, True, False, True])
    assert pieza.get_status_ok() == [True, False, True, False, True]


def test_get_status_ok_val(pieza):
    pieza.set_status_ok([True, False, True, False, True])
    assert pieza.get_status_ok_val(4) == True

def test_set_status_ok_val(pieza):
    pieza.set_status_ok_val(False, 4)
    assert pieza.get_status_ok_val(4) == False
