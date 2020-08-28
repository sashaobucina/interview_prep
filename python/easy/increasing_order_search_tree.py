class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and (self.right == other.right)


def increasing_BST(root: TreeNode) -> TreeNode:
    """
    # 897: Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the 
    tree is now the root of the tree, and every node has no left child and only 1 right child.
    """
    dummy = TreeNode(0)
    curr = dummy

    def inorder(node):
        nonlocal curr

        if not node:
            return

        inorder(node.left)

        node.left = None
        curr.right = node
        curr = node

        inorder(node.right)

    inorder(root)
    return dummy.right


if __name__ == "__main__":
    # construct BST
    n5 = TreeNode(4)
    n4 = TreeNode(1)
    n3 = TreeNode(3, left=n4, right=n5)
    n2 = TreeNode(6)
    n1 = TreeNode(5, left=n3, right=n2)

    # construct expected BST
    _n5 = TreeNode(6)
    _n4 = TreeNode(5, right=_n5)
    _n3 = TreeNode(4, right=_n4)
    _n2 = TreeNode(3, right=_n3)
    _n1 = TreeNode(1, right=_n2)

    assert increasing_BST(n1) == _n1

    print("Passed all tests!")
