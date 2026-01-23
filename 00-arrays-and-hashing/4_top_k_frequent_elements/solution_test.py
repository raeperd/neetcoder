from .solution import Solution


def test_example_1():
    result = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == sorted([1, 2])


def test_example_2():
    assert Solution().topKFrequent([1], 1) == [1]


def test_example_3():
    result = Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)
    assert sorted(result) == sorted([1, 2])
