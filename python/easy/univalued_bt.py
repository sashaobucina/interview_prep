class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_unival_tree(root: TreeNode) -> bool:
    """
    # 965: A binary tree is univalued if every node in the tree has the same value.

    Return true if and only if the given tree is univalued.
    """
    def traverse(root: TreeNode) -> bool:
        if not root:
            return True

        if root.val != val:
            return False

        return traverse(root.left) and traverse(root.right)

    val = root.val
    return traverse(root)


def is_unival_tree_iter(root: TreeNode) -> bool:
    stk = [root]
    while stk:
        curr = stk.pop()

        if curr.val != root.val:
            return False

        if curr.left:
            stk.append(curr.left)
        if curr.right:
            stk.append(curr.right)

    return True


if __name__ == "__main__":
    n3 = TreeNode(1)
    n2 = TreeNode(1)
    n1 = TreeNode(1, left=n2, right=n3)
    assert is_unival_tree(n1)
    assert is_unival_tree_iter(n1)

    n3.left = TreeNode(2)
    assert not is_unival_tree(n1)
    assert not is_unival_tree_iter(n1)

    print("Passed all tests!")
