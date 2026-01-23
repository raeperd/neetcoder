from .solution import my_pow


def test_example_1():
    assert abs(my_pow(2.00000, 10) - 1024.00000) < 0.00001


def test_example_2():
    assert abs(my_pow(2.10000, 3) - 9.26100) < 0.00001


def test_example_3():
    assert abs(my_pow(2.00000, -2) - 0.25000) < 0.00001
