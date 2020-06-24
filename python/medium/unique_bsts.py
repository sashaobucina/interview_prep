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


if __name__ == "__main__":
    expected = [1, 2, 5, 14, 42, 132, 429, 1430]

    for i in range(1, 8):
        assert num_BSTs(i) == expected[i - 1]

    print("Passed all tests!")
