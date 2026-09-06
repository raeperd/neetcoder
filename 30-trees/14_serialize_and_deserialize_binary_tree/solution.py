class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        raise NotImplementedError("Implement Codec.serialize")

    def deserialize(self, data: str) -> TreeNode:
        raise NotImplementedError("Implement Codec.deserialize")
