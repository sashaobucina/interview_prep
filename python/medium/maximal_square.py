from typing import List


def maximal_square(matrix: List[List[int]]) -> int:
    """
    # 221: Given a 2D binary matrix filled with 0's and 1's, find the largest square containing 
    only 1's and return its area.
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Base case
    max_so_far = 0
    for i in range(m):
        dp[i][0] = int(matrix[i][0])
        if dp[i][0]:
            max_so_far = 1

    for i in range(n):
        dp[0][i] = int(matrix[0][i])
        if dp[0][i]:
            max_so_far = 1

    # Recurrence relation: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == "1":
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                ) + 1
                max_so_far = max(max_so_far, dp[i][j])

    return max_so_far * max_so_far


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "1"]
    ]
    assert maximal_square(matrix) == 4

    print("Passed all tests!")
