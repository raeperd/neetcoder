from .solution import threeSum


def test_example_1():
    result = threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    # Sort each triplet and the list of triplets for comparison
    result = sorted([sorted(triplet) for triplet in result])
    expected = sorted([sorted(triplet) for triplet in expected])
    assert result == expected


def test_example_2():
    assert threeSum([0, 1, 1]) == []


def test_example_3():
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
