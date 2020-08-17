from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    # 173: Implement an iterator over a binary search tree (BST). Your iterator will be initialized 
    with the root node of a BST.

    Calling next() will return the next smallest number in the BST.

    NOTE:
        - next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height 
            of the tree.
        - You may assume that next() call will always be valid, that is, there will be at least a next 
            smallest number in the BST when next() is called.
    """

    def __init__(self, root: TreeNode):
        self.stk = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode) -> None:
        while node:
            self.stk.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stk.pop()
        if node.right:
            self._leftmost_inorder(node.right)

        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stk) > 0


if __name__ == "__main__":
    # construct BST
    n5 = TreeNode(20)
    n4 = TreeNode(9)
    n3 = TreeNode(15, left=n4, right=n5)
    n2 = TreeNode(3)
    n1 = TreeNode(7, left=n2, right=n3)

    iterator = BSTIterator(n1)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext()
    assert iterator.next() == 9
    assert iterator.next() == 15
    assert iterator.hasNext()
    assert iterator.next() == 20
    assert not iterator.hasNext()

    print("Passed all tests!")
