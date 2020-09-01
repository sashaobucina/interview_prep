class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) \
            and (self.right == other.right)


def delete_node(root: TreeNode, key: int) -> TreeNode:
    """
    # 450: Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
    Return the root node reference (possibly updated) of the BST.

    Basically, the deletion can be divided into two stages:
        - Search for a node to remove.
        - If the node is found, delete the node.

    NOTE: Time complexity should be O(height of tree).
    """
    def _search(node, parent, is_left):
        if not node:
            return

        if node.val == key:
            _delete_node(node, parent, is_left)

        if node.left and key < node.val:
            _search(node.left, node, True)
        elif node.right and key > node.val:
            _search(node.right, node, False)

    def _delete_node(node, parent, left):
        nonlocal root

        right_sub = node.right
        while right_sub and right_sub.left:
            right_sub = right_sub.left

        if right_sub:
            right_sub.left = node.left

        if parent:
            if left:
                if node.right:
                    parent.left = node.right
                else:
                    parent.left = node.left
            else:
                if node.right:
                    parent.right = node.right
                else:
                    parent.right = node.left
        else:
            if node.right:
                root = node.right
            else:
                root = node.left

    _search(root, None, False)
    return root


if __name__ == "__main__":
    # construct input BST
    n6 = TreeNode(7)
    n5 = TreeNode(4)
    n4 = TreeNode(2)
    n3 = TreeNode(6, right=n6)
    n2 = TreeNode(3, left=n4, right=n5)
    n1 = TreeNode(5, left=n2, right=n3)

    # construct expected output BST
    _n5 = TreeNode(7)
    _n4 = TreeNode(2)
    _n3 = TreeNode(6, right=_n5)
    _n2 = TreeNode(4, left=_n4)
    _n1 = TreeNode(5, left=_n2, right=_n3)

    delete_node(n1, 3)
    assert n1 == _n1

    print("Passed all tests!")
