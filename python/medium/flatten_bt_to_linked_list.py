from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) \
            and (self.right == other.right)


def flatten(root: TreeNode) -> None:
    """
    # 114: Given a binary tree, flatten it to a linked list in-place.

        1
       / \
      2   5
     / \   \
    3   4   6

    converts to

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
    """
    def _flatten(node: TreeNode) -> Optional[TreeNode]:
        if not node:
            return None

        if not node.left and not node.right:
            return node

        # flatten subtrees and get the tails of both sides
        left_tail = _flatten(node.left)
        right_tail = _flatten(node.right)

        # shuffle BT to only have right nodes in subtree
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    _flatten(root)


if __name__ == "__main__":
    # build original tree
    n6 = TreeNode(6)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n5 = TreeNode(5, right=n6)
    n2 = TreeNode(2, left=n3, right=n4)
    n1 = TreeNode(1, left=n2, right=n5)

    # build expected tree
    e6 = TreeNode(6)
    e5 = TreeNode(5, right=e6)
    e4 = TreeNode(4, right=e5)
    e3 = TreeNode(3, right=e4)
    e2 = TreeNode(2, right=e3)
    e1 = TreeNode(1, right=e2)

    flatten(root=n1)
    assert n1 == e1

    print("Passed all tests!")
