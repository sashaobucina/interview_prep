from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


def build_tree(pre: List[int], post: List[int]) -> TreeNode:
    """
    # 889: Return any binary tree that matches the given preorder and postorder traversals.

    Values in the traversals pre and post are distinct positive integers.
    """
    if not pre:
        return None

    root = TreeNode(pre[0])

    if len(pre) == 1:
        return root

    L = post.index(pre[1]) + 1

    root.left = build_tree(pre[1:L+1], post[:L])
    root.right = build_tree(pre[L+1:], post[L:-1])

    return root


if __name__ == "__main__":
    # construct expected result BT
    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n6, right=n7)
    n2 = TreeNode(2, left=n4, right=n5)
    n1 = TreeNode(1, left=n2, right=n3)

    pre, post = [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]
    assert build_tree(pre, post) == n1
    print("Passed all tests!")
