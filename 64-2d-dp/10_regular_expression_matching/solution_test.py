from .solution import is_match


def test_example_1():
    assert is_match("aa", "a") == False


def test_example_2():
    assert is_match("aa", "a*") == True


def test_example_3():
    assert is_match("ab", ".*") == True
