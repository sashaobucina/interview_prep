from typing import List
from itertools import product


def num_BSTs(n: int) -> int:
    """
    # 96: Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
    """
    memo = [0] * (n + 1)

    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            memo[i] += memo[j - 1] * memo[i - j]

    return memo[n]


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_BSTs(n: int) -> List[TreeNode]:
    """
    # 95: Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
    """
    def _helper(m, n):
        if m > n:
            return [None]

        ans = []
        for i in range(m, n+1):
            ls = _helper(m, i-1)
            rs = _helper(i + 1, n)
            for l, r in product(ls, rs):
                ans.append(TreeNode(i, l, r))

        return ans

    if n == 0:
        return []
    return _helper(1, n)


if __name__ == "__main__":
    expected = [1, 2, 5, 14, 42, 132, 429, 1430]
    for i in range(1, 8):
        assert num_BSTs(i) == expected[i - 1]

    print("Passed all tests!")
