from .solution import word_break


def test_example_1():
    assert word_break("leetcode", ["leet", "code"]) == True


def test_example_2():
    assert word_break("applepenapple", ["apple", "pen"]) == True


def test_example_3():
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
