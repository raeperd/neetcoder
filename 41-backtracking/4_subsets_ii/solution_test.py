from .solution import Solution


def test_subsets_with_dup_example1():
    nums = [1, 2, 2]
    result = Solution().subsetsWithDup(nums)
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_subsets_with_dup_example2():
    nums = [0]
    result = Solution().subsetsWithDup(nums)
    expected = [[], [0]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
