class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_prodcut(root: TreeNode) -> int:
    """
    # 1339: Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that 
    the product of the sums of the subtrees are maximized.

    Since the answer may be too large, return it modulo 10^9 + 7.
    """
    def find_sum(root):
        if not root:
            return 0
        return root.val + find_sum(root.left) + find_sum(root.right)

    total_sum = find_sum(root)

    # perform DFS to get subtree sums and save them for later
    ans = 0

    def subtree_sum(node):
        nonlocal ans
        if not node:
            return 0
        _sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
        ans = max(ans, _sum * (total_sum - _sum))
        return _sum

    subtree_sum(root)
    return ans % ((10**9) + 7)


if __name__ == "__main__":
    # construct BT
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n6)
    n2 = TreeNode(2, left=n4, right=n5)
    n1 = TreeNode(1, left=n2, right=n3)
    assert max_prodcut(n1) == 110

    print("Passed all tests!")
