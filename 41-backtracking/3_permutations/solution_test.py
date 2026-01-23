from .solution import permute


def test_permute_example1():
    nums = [1, 2, 3]
    result = permute(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(result) == sorted(expected)


def test_permute_example2():
    nums = [0, 1]
    result = permute(nums)
    expected = [[0, 1], [1, 0]]
    assert sorted(result) == sorted(expected)


def test_permute_example3():
    nums = [1]
    result = permute(nums)
    expected = [[1]]
    assert result == expected
