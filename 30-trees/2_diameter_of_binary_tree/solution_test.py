from typing import Optional

from .solution import TreeNode, diameter_of_binary_tree


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


def test_diameter_example1():
    root = build_tree([1, 2, 3, 4, 5])
    assert diameter_of_binary_tree(root) == 3


def test_diameter_example2():
    root = build_tree([1, 2])
    assert diameter_of_binary_tree(root) == 1
