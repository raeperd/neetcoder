from .solution import letter_combinations


def test_letter_combinations_example1():
    digits = "23"
    result = letter_combinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result) == sorted(expected)


def test_letter_combinations_example2():
    digits = ""
    result = letter_combinations(digits)
    assert result == []


def test_letter_combinations_example3():
    digits = "2"
    result = letter_combinations(digits)
    expected = ["a", "b", "c"]
    assert sorted(result) == sorted(expected)
