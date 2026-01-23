from .solution import longest_palindrome


def test_example_1():
    result = longest_palindrome("babad")
    assert result in ["bab", "aba"]


def test_example_2():
    assert longest_palindrome("cbbd") == "bb"
