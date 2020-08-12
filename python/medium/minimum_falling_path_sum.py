from typing import List


def min_falling_path_sum(A: List[List[int]]) -> int:
    """
    # 931: Given a square array of integers A, we want the minimum sum of a falling path through A.

    A falling path starts at any element in the first row, and chooses one element from each row. The next 
    row's choice must be in a column that is different from the previous row's column by at most one.
    """
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case
    for i in range(n):
        dp[0][i] = A[0][i]

    # Recurrence relation: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]
    for i in range(1, n):
        for j in range(n):
            left = dp[i - 1][j - 1] if j > 0 else float("inf")
            mid = dp[i - 1][j]
            right = dp[i - 1][j + 1] if j < n - 1 else float("inf")

            dp[i][j] = min(left, mid, right) + A[i][j]

    return min(dp[n - 1])


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert min_falling_path_sum(A) == 12

    A = [
        [7, 81, 74, 65, 90, 74, 47, 46, 71, 55],
        [50, 47, 63, 71, 26, 39, 17, 28,  8, 48],
        [74, 43, 87,  9,  2, 34, 78, 99, 63, 13],
        [46, 55, 95, 23, 26, 75, 44, 50, 55, 41],
        [8, 33, 38, 16, 24, 31, 44, 83, 75, 63],
        [64, 43, 91, 37, 13, 53, 64, 2, 24, 83],
        [39, 52, 98, 13, 48, 45, 74, 3, 79, 19],
        [49, 97, 19, 76, 42, 29, 78, 64,  2, 62],
        [38,  1, 16, 44, 59, 33, 62, 15, 79, 33],
        [76, 52, 61,  9, 42, 75, 10, 58, 81, 84]
    ]
    assert min_falling_path_sum(A) == 197

    print("Passed all tests!")
