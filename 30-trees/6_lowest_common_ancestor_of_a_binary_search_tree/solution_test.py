from typing import Optional

from .solution import TreeNode, lowest_common_ancestor


def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    nodes = {}
    root = TreeNode(values[0])
    nodes[values[0]] = root
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            nodes[values[i]] = node.left
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            nodes[values[i]] = node.right
            queue.append(node.right)
        i += 1
    return root, nodes


def test_lca_example1():
    root, nodes = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = nodes[2]
    q = nodes[8]
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 6


def test_lca_example2():
    root, nodes = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = nodes[2]
    q = nodes[4]
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 2


def test_lca_example3():
    root, nodes = build_tree([2, 1])
    p = nodes[2]
    q = nodes[1]
    result = lowest_common_ancestor(root, p, q)
    assert result.val == 2
