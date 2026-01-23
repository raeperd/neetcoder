from .solution import count_bits


def test_example_1():
    assert count_bits(2) == [0, 1, 1]


def test_example_2():
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
