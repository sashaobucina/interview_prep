class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    """
    # 872: Consider all the leaves of a binary tree, from left to right order, the values of those leaves 
    form a leaf value sequence.

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
    """
    def leaf_sequence(root, ans):
        if not root:
            return

        if not root.left and not root.right:
            ans.append(root.val)
            return
        
        if root.left:
            leaf_sequence(root.left, ans)
        if root.right:
            leaf_sequence(root.right, ans)
            
    l1, l2 = [], []
    leaf_sequence(root1, l1)
    leaf_sequence(root2, l2)
    
    return l1 == l2


if __name__ == "__main__":
    # construct first tree
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    assert leaf_similar(n1, n2)

    # construct second tree
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    assert not leaf_similar(n1, n2)


    print("Passed all tests!")