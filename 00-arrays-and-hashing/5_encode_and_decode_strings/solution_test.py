from .solution import decode, encode


def test_example_1():
    strs = ["Hello", "World"]
    encoded = encode(strs)
    assert decode(encoded) == strs


def test_empty_strings():
    strs = ["", ""]
    encoded = encode(strs)
    assert decode(encoded) == strs


def test_special_characters():
    strs = ["Hello", "World", "with#special", "chars"]
    encoded = encode(strs)
    assert decode(encoded) == strs
