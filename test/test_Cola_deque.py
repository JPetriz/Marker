import pytest

from cola_deque import ColaDeque
from trailer_hitch import TrailerHitch

@pytest.fixture
def cola():
    return ColaDeque()

def test_is_empty(cola):
    assert cola.is_empty() is True


def test_queue(cola):
    cola.queue(1)
    assert cola.is_empty() is False


def test_dequeue(cola):
    cola.queue(1)
    cola.dequeue()
    assert cola.is_empty() is True


def test_front(cola):
    cola.queue(9)
    assert cola.front() == 9


def test_size(cola):
    cola.queue(9)
    cola.queue(10)
    assert cola.size() == 2

def test_queue_trailer(cola):
    pieza1 = TrailerHitch([1, 2, 3, 4, 5], 10, 8, True, "TBD")
    pieza2 = TrailerHitch([5, 6, 7, 8, 9], 12, 6, True, "ABC")
    cola.queue(pieza1)
    cola.queue(pieza2)
    assert cola.dequeue() == pieza1