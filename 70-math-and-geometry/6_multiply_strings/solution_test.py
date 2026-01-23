from .solution import multiply


def test_example_1():
    assert multiply("2", "3") == "6"


def test_example_2():
    assert multiply("123", "456") == "56088"
