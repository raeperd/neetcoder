import pytest

from .solution import Solution


def assert_round_trip(strs):
    encoded = Solution().encode(strs)
    assert isinstance(encoded, str)
    assert Solution().decode(encoded) == strs


def test_example_1():
    strs = ["Hello", "World"]
    assert_round_trip(strs)


def test_empty_strings():
    strs = ["", ""]
    assert_round_trip(strs)


def test_special_characters():
    strs = ["Hello", "World", "with#special", "chars"]
    assert_round_trip(strs)


@pytest.mark.parametrize(
    "strs",
    [
        [""],
        ["#", "##", "1#", "12#payload", "", ",", ":", "\n", "\x00"],
        ["a" * 200, "b" * 200],
        ["same"] * 200,
        ["".join(chr(i) for i in range(128)), "".join(chr(i) for i in range(128, 256))],
    ],
)
def test_round_trip_boundaries(strs):
    assert_round_trip(strs)


def test_encodings_are_independent():
    encoder = Solution()
    first = encoder.encode(["first", ""])
    second = encoder.encode(["second", "#"])
    assert isinstance(first, str)
    assert isinstance(second, str)
    decoder = Solution()
    assert decoder.decode(second) == ["second", "#"]
    assert decoder.decode(first) == ["first", ""]
