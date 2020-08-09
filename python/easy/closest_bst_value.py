class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root: TreeNode, target: float) -> int:
    """
    # 270: Given a non-empty binary search tree and a target value, find the value in the BST that 
    is closest to the target.

    NOTE:
        - Given target value is a floating point.
        - You are guaranteed to have only one unique value in the BST that is closest to the target.
    """
    val = None
    diff = float("inf")

    def helper(root):
        nonlocal diff
        nonlocal val

        if not root:
            return

        _diff = target - root.val
        if abs(_diff) < diff:
            diff = abs(_diff)
            val = root.val

        if _diff > 0:
            helper(root.right)
        else:
            helper(root.left)

    helper(root)
    return val


if __name__ == "__main__":
    n5 = TreeNode(5)
    n4 = TreeNode(3)
    n3 = TreeNode(1)
    n2 = TreeNode(2, left=n3, right=n4)
    n1 = TreeNode(4, left=n2, right=n5)

    assert closest_value(n1, 3.714286) == 4

    print("Passed all tests!")
