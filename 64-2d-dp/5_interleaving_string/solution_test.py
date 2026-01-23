from .solution import is_interleave


def test_example_1():
    assert is_interleave("aabcc", "dbbca", "aadbbcbcac") == True


def test_example_2():
    assert is_interleave("aabcc", "dbbca", "aadbbbaccc") == False


def test_example_3():
    assert is_interleave("", "", "") == True
