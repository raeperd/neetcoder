import pytest

from .solution import findMedianSortedArrays


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ],
)
def test_findMedianSortedArrays(nums1, nums2, expected):
    assert findMedianSortedArrays(nums1, nums2) == expected
