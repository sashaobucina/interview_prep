from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


class Codec:
    """
    # 297: Serialization is the process of converting a data structure or object into a sequence of 
    bits so that it can be stored in a file or memory buffer, or transmitted across a network connection
    link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how 
    your serialization/deserialization algorithm should work. 

    You just need to ensure that a binary tree can be serialized to a string and this string can be 
    deserialized to the original tree structure.

    This solution uses DFS w/ preorder traversal.
    """

    def serialize(self, root: TreeNode) -> str:
        data = []

        def rserialize(root: TreeNode) -> None:
            if not root:
                data.append(None)
                return

            data.append(root.val)
            rserialize(root.left)
            rserialize(root.right)

        rserialize(root)
        return str(data)[1:-1]

    def deserialize(self, data: str) -> TreeNode:
        if data == "":
            return None

        def rdeserialize(l: List[str]) -> Optional[TreeNode]:
            if l[0] == "None":
                l.popleft()
                return None

            val = int(l.popleft())
            root = TreeNode(val)

            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

            return root

        data = data.split(", ")
        root = rdeserialize(deque(data))
        return root


if __name__ == "__main__":
    # construct original BT
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n4, right=n5)
    n2 = TreeNode(2)
    n1 = TreeNode(1, left=n2, right=n3)

    # ensure after serialization & deserialization, tree is reconstructed in same way
    codec = Codec()
    assert codec.deserialize(codec.serialize(n1)) == n1
    assert codec.deserialize(codec.serialize(None)) is None

    print("Passed all tests!")
