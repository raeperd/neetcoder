from .solution import reverse_bits


def test_example_1():
    assert reverse_bits(43261596) == 964176192


def test_example_2():
    assert reverse_bits(2147483644) == 1073741822
