def min_distance(word1: str, word2: str) -> int:
    """
    # 72: Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

    You have the following 3 operations permitted on a word:
        1) Insert a character
        2) Delete a character
        3) Replace a character

    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    m, n = len(word2), len(word1)
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case
    for i in range(1, n + 1):
        memo[0][i] = i
    for i in range(1, m + 1):
        memo[i][0] = i

    # Recurrence relation:
    #   Lev(i, j) = min(Lev(i - 1, j) + 1, Lev(i, j - 1) + 1, Lev(i - 1, j - 1) + 1 <- (if a[i] != b[j]))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = memo[i][j - 1] + 1
            deletion = memo[i - 1][j] + 1
            replacement = memo[i - 1][j - 1] + 1 if word1[j - 1] != word2[i - 1] else memo[i - 1][j - 1]

            memo[i][j] = min(insertion, deletion, replacement)

    return memo[m][n]


def min_distance_naive(word1: str, word2: str) -> int:
    """
    Naive implementation of edit distance using recursive approach.

    Lev(i, j) = min(Lev(i - 1, j) + 1, Lev(i, j - 1) + 1, Lev(i - 1, j - 1) + 1 if a[j] != b[j])
        Lev(i - 1, j) -> Deletion of last ch in word1 after a[:i-1] == b[:j]
        Lev(i, j - 1) -> Insertion of last ch in word2 after a[:i] == b[:j-1]
        Lev(i - 1, j - 1) -> Replacement of last ch if not same, after a[:i-1] == b[:j-1]
    """
    def lev(i, j) -> int:
        if i == 0 or j == 0:
            return max(i, j)

        deletion = lev(i - 1, j) + 1
        insertion = lev(i, j - 1) + 1
        replacement = lev(i - 1, j - 1)
        if word1[i - 1] != word2[j - 1]:
            replacement += 1

        return min(deletion, insertion, replacement)

    return lev(len(word1), len(word2))


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance_naive("horse", "ros") == 3

    assert min_distance("kitten", "sitting") == 3
    assert min_distance_naive("kitten", "sitting") == 3

    assert min_distance("intention", "execution") == 5
    assert min_distance_naive("intention", "execution") == 5

    print("Passed all tests!")
