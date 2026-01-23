from .solution import hamming_weight


def test_example_1():
    assert hamming_weight(11) == 3


def test_example_2():
    assert hamming_weight(128) == 1


def test_example_3():
    assert hamming_weight(2147483645) == 30
