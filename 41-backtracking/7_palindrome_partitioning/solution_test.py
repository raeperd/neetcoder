from .solution import Solution


def test_partition_example1():
    s = "aab"
    result = Solution().partition(s)
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(result) == sorted(expected)


def test_partition_example2():
    s = "a"
    result = Solution().partition(s)
    expected = [["a"]]
    assert result == expected
