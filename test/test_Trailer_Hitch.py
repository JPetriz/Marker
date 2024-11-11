import pytest

from trailer_hitch import TrailerHitch

@pytest.fixture
def barra():
    return TrailerHitch([1, 2, 3, 4, 5], 10, 8, True, "TBD")


def test_get_characters(barra):
    assert barra.get_characters() == [1, 2, 3, 4, 5]


def test_set_characters(barra):
    barra.set_characters([5, 4, 3, 2, 1])
    assert barra.get_characters() == [5, 4, 3, 2, 1]


def test_get_character_val(barra):
    assert barra.get_character_val(4) == 5


def test_set_character_val(barra):
    barra.set_character_val(8,4)
    assert barra.get_character_val(4) == 8


def test_get_part_number(barra):
    assert barra.get_part_number() == 10


def test_set_part_number(barra):
    barra.set_part_number(8)
    assert barra.get_part_number() == 8


def test_get_series(barra):
    assert barra.get_series() == 8


def test_set_series(barra):
    barra.set_series(9)
    assert barra.get_series() == 9


def test_get_status_ok(barra):
    assert barra.get_status_ok() == True


def test_set_status_ok(barra):
    barra.set_status_ok(False)
    assert barra.get_status_ok() == False


def test_get_date(barra):
    assert barra.get_date() == "TBD"


def test_set_date(barra):
    barra.set_date("PSD")
    assert barra.get_date() == "PSD"


def test_get_model(barra):
    assert False


def test_get_status(barra):
    assert barra.get_status() == "AUDIOZ02"


def test_get_steps_number(barra):
    assert barra.get_steps_number() == 4
