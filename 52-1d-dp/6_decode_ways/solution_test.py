from .solution import num_decodings


def test_example_1():
    assert num_decodings("12") == 2


def test_example_2():
    assert num_decodings("226") == 3


def test_example_3():
    assert num_decodings("06") == 0
