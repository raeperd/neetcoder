from .solution import longest_common_subsequence


def test_example_1():
    assert longest_common_subsequence("abcde", "ace") == 3


def test_example_2():
    assert longest_common_subsequence("abc", "abc") == 3


def test_example_3():
    assert longest_common_subsequence("abc", "def") == 0
