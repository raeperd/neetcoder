from .solution import reverse


def test_example_1():
    assert reverse(123) == 321


def test_example_2():
    assert reverse(-123) == -321


def test_example_3():
    assert reverse(120) == 21
