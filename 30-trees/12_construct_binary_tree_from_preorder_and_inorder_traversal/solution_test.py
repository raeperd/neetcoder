from typing import Optional

from .solution import TreeNode, build_tree


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


def test_build_tree_example1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = build_tree(preorder, inorder)
    assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]


def test_build_tree_example2():
    preorder = [-1]
    inorder = [-1]
    result = build_tree(preorder, inorder)
    assert tree_to_list(result) == [-1]
