from typing import Optional

from .solution import TreeNode, invert_tree


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
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def test_invert_tree_example1():
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    result = invert_tree(root)
    assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]


def test_invert_tree_example2():
    root = build_tree([2, 1, 3])
    result = invert_tree(root)
    assert tree_to_list(result) == [2, 3, 1]


def test_invert_tree_example3():
    root = build_tree([])
    result = invert_tree(root)
    assert tree_to_list(result) == []
