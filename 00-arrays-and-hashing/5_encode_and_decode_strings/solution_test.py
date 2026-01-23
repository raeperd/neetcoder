from .solution import Solution


def test_example_1():
    strs = ["Hello", "World"]
    encoded = Solution().encode(strs)
    assert Solution().decode(encoded) == strs


def test_empty_strings():
    strs = ["", ""]
    encoded = Solution().encode(strs)
    assert Solution().decode(encoded) == strs


def test_special_characters():
    strs = ["Hello", "World", "with#special", "chars"]
    encoded = Solution().encode(strs)
    assert Solution().decode(encoded) == strs
