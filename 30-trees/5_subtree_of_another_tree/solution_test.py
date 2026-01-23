from typing import Optional

from .solution import TreeNode, is_subtree


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


def test_is_subtree_example1():
    root = build_tree([3, 4, 5, 1, 2])
    sub_root = build_tree([4, 1, 2])
    assert is_subtree(root, sub_root) == True


def test_is_subtree_example2():
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub_root = build_tree([4, 1, 2])
    assert is_subtree(root, sub_root) == False
