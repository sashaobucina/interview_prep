from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode) -> int:
    """
    # 337: The thief has found himself a new place for his thievery again. There is only one entrance 
    to this area, called the "root." Besides the root, each house has one and only one parent house. 
    After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
    It will automatically contact the police if two directly-linked houses were broken into on the same night.

    Determine the maximum amount of money the thief can rob tonight without alerting the police.
    """
    def helper(root: TreeNode) -> Tuple[int]:
        if not root:
            return (0, 0)

        with_l, without_l = helper(root.left)
        with_r, without_r = helper(root.right)

        return (root.val + without_l + without_r, max(with_l, without_l) + max(with_r, without_r))

    return max(helper(root))


if __name__ == "__main__":
    # construct BT
    n5 = TreeNode(1)
    n4 = TreeNode(3)
    n3 = TreeNode(3, right=n5)
    n2 = TreeNode(2, right=n4)
    n1 = TreeNode(3, left=n2, right=n3)

    assert rob(n1) == 7

    print("Passed all tests!")
