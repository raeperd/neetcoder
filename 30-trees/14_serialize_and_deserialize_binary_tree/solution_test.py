from typing import Optional

import pytest

from .solution import Codec, TreeNode


def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node:
            assert id(node) not in visited, "Decoded tree contains a cycle or a shared child"
            visited.add(id(node))
            assert len(visited) <= 10_000, "Decoded tree exceeds the problem's node limit"
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def assert_round_trip(values):
    serialized = Codec().serialize(build_tree(values))
    assert isinstance(serialized, str)
    deserialized = Codec().deserialize(serialized)
    assert tree_to_list(deserialized) == values


def test_serialize_deserialize_example1():
    assert_round_trip([1, 2, 3, None, None, 4, 5])


def test_serialize_deserialize_example2():
    assert_round_trip([])


@pytest.mark.parametrize("values", [[0], [-1000, None, 1000], [1, 1, 1], [1, 2, None, 3]])
def test_round_trip_boundaries(values):
    assert_round_trip(values)


def test_encodings_are_independent():
    encoder = Codec()
    first = encoder.serialize(build_tree([1, None, 2]))
    second = encoder.serialize(build_tree([-1, -2, -3]))
    assert isinstance(first, str)
    assert isinstance(second, str)
    decoder = Codec()
    assert tree_to_list(decoder.deserialize(second)) == [-1, -2, -3]
    assert tree_to_list(decoder.deserialize(first)) == [1, None, 2]
