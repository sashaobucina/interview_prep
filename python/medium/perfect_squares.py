from collections import deque


def perfect_square(n: int) -> int:
    """
    # 279: Given a positive integer n, find the least number of perfect square numbers 
    (for example, 1, 4, 9, 16, ...) which sum to n.

    This sol'n uses an iterative dynamic programming apporach.

    Time complexity: O(n^3/2)
    Space complexity: O(n)
    """
    memo = [0] + [float("inf")] * n
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            memo[i] = min(memo[i], memo[i - j * j] + 1)
            j += 1

    return memo[n]


def perfect_square_bfs(n: int) -> int:
    """
    This solution uses an iterative bfs approach.

    Time complexity: O(n^3/2)
    Space complexity: O(n)
    """
    q = deque([n])

    count = 0
    while q:
        # go through bfs and keep track of levels
        level = len(q)

        for i in range(level):
            curr = q.pop()

            # iterate through squares
            j = 1
            while j * j <= curr:
                if curr == j * j:
                    return count + 1

                q.appendleft(curr - j * j)
                j += 1

        # increment count
        count += 1

    # should not be here if given a positive integer
    raise ValueError("Positive integer should be given!")



if __name__ == "__main__":
    assert perfect_square(12) == perfect_square_bfs(12) == 3
    assert perfect_square(13) == perfect_square_bfs(13) == 2

    print("Passed all tests!")