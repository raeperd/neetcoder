from .solution import Solution


def test_subsets_example1():
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_subsets_example2():
    nums = [0]
    result = Solution().subsets(nums)
    expected = [[], [0]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
