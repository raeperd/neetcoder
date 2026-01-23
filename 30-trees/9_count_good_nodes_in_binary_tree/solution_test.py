from typing import Optional

from .solution import TreeNode, good_nodes


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


def test_good_nodes_example1():
    root = build_tree([3, 1, 4, 3, None, 1, 5])
    assert good_nodes(root) == 4


def test_good_nodes_example2():
    root = build_tree([3, 3, None, 4, 2])
    assert good_nodes(root) == 3


def test_good_nodes_example3():
    root = build_tree([1])
    assert good_nodes(root) == 1
