from .solution import isAnagram


def test_example_1():
    assert isAnagram("anagram", "nagaram") == True


def test_example_2():
    assert isAnagram("rat", "car") == False
