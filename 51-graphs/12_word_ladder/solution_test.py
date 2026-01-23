from .solution import ladder_length


def test_example_1():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_example_2():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
