from .solution import count_substrings


def test_example_1():
    assert count_substrings("abc") == 3


def test_example_2():
    assert count_substrings("aaa") == 6
