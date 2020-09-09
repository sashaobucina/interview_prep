from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return type(self) == type(other) and self.val == other.val and self.left == other.left and self.right == other.right


def delete_nodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    """
    # 1110: Given the root of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

    Return the roots of the trees in the remaining forest.  You may return the result in any order.
    """
    def postorder(root):
        if not root:
            return None

        root.left = postorder(root.left)
        root.right = postorder(root.right)

        if root.val in to_delete:
            to_delete.remove(root.val)

            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)

            root = None

        return root

    ans = []
    to_delete = set(to_delete)
    if root.val not in to_delete:
        ans.append(root)

    postorder(root)
    return ans


if __name__ == "__main__":
    # construct input tree
    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n6, right=n7)
    n2 = TreeNode(2, left=n4, right=n5)
    n1 = TreeNode(1, left=n2, right=n3)

    # construct expected forest
    _n4 = TreeNode(4)
    _n2 = TreeNode(2, left=_n4)
    _n1 = TreeNode(1, left=_n2)
    expected_forest = [_n1, TreeNode(6), TreeNode(7)]

    assert delete_nodes(n1, [3, 5]) == expected_forest

    print("Passed all tests!")
