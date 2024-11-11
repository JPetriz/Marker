import pytest

from register import Register

@pytest.fixture
def registro():
    return Register("TBD", 123, 10002, 6, 1.5, True, "AUDI_",
                    "5", "20", "9", "13")


def test_get_date(registro):
    assert registro.get_date() == "TBD"


def test_set_date(registro):
    registro.set_date("ABC")
    assert registro.get_date() == "ABC"


def test_get_character(registro):
    assert registro.get_character() == 123


def test_set_character(registro):
    registro.set_character(456)
    assert registro.get_character() == 456


def test_get_program(registro):
    assert registro.get_program() == 10002


def test_set_program(registro):
    registro.set_program(2002)
    assert registro.get_program() == 2002


def test_get_serie(registro):
    assert registro.get_serie() == 6


def test_set_serie(registro):
    registro.set_serie(5)
    assert registro.get_serie() == 5


def test_get_score(registro):
    assert registro.get_score() == 1.5


def test_set_score(registro):
    registro.set_score(4.8)
    assert registro.get_score() == 4.8


def test_get_status_ok(registro):
    assert registro.get_status_ok() == True


def test_set_status_ok(registro):
    registro.set_status_ok(False)
    assert registro.get_status_ok() == False


def test_get_mark(registro):
    assert registro.get_mark() == "AUDI_"


def test_set_mark(registro):
    registro.set_mark("BR167N")
    assert registro.get_mark() == "BR167N"


def test_get_voltage(registro):
    assert registro.get_voltage() == "5"


def test_set_voltage(registro):
    registro.set_voltage("8.7")
    assert registro.get_voltage() == "8.7"


def test_get_current(registro):
    assert registro.get_current() == "20"


def test_set_current(registro):
    registro.set_current("12.2")
    assert registro.get_current() == "12.2"


def test_get_wire(registro):
    assert registro.get_wire() == "9"


def test_set_wire(registro):
    registro.set_wire("30.8")
    assert registro.get_wire() == "30.8"


def test_get_gas(registro):
    assert registro.get_gas() == "13"

def test_set_gas(registro):
    registro.set_gas("54.7")
    assert registro.get_gas() == "54.7"


def test_compare_to():
    assert False
