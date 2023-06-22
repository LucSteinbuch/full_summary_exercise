from example import add
from example import subtract


def test_add():
    assert add(1, 2) == 3
    assert add(2, 8) == 10


def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(8, 2) == 6
