class TreeNode:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def inorder_successor(node: TreeNode) -> TreeNode:
    """
    # 510: Given a node in a binary search tree, find the in-order successor of that
    node in the BST.

    If that node has no in-order successor, return null.

    The successor of a node is the node with the smallest key greater than node.val.

    You will have direct access to the node but not to the root of the tree. Each
    node will have a reference to its parent node.
    """
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent


if __name__ == "__main__":
    n3 = TreeNode(3)
    n2 = TreeNode(1)
    n1 = TreeNode(2, left=n2, right=n3)
    n2.parent = n1
    n3.parent = n1

    assert inorder_successor(n1).val == 3

    print("Passed all tests!")
