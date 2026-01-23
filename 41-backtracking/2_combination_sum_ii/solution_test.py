from .solution import Solution


def test_combination_sum2_example1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = Solution().combinationSum2(candidates, target)
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_combination_sum2_example2():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    result = Solution().combinationSum2(candidates, target)
    expected = [[1, 2, 2], [5]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
