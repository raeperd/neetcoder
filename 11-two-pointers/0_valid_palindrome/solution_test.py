from .solution import isPalindrome


def test_example_1():
    assert isPalindrome("A man, a plan, a canal: Panama") == True


def test_example_2():
    assert isPalindrome("race a car") == False


def test_example_3():
    assert isPalindrome(" ") == True
