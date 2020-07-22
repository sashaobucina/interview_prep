from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    """
    # 103: Given a binary tree, return the zigzag level order traversal of its nodes' values. 
    (ie, from left to right, then right to left for the next level and alternate between).
    """
    if not root:
        return []

    ans = []

    ltr = True
    next_level = []
    curr_level = [root]
    while curr_level:
        ans.append([node.val for node in curr_level[::-1]])

        for _ in range(len(curr_level)):
            curr = curr_level.pop()

            if ltr:
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            else:
                if curr.right:
                    next_level.append(curr.right)
                if curr.left:
                    next_level.append(curr.left)

        curr_level, next_level = next_level, curr_level
        ltr = not ltr

    return ans


if __name__ == "__main__":
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, left=n4, right=n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, left=n2, right=n3)
    assert zigzag_level_order(root=n1) == [[3], [20, 9], [15, 7]]

    print("Passed all tests!")
