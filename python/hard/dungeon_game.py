from typing import List


def calculate_min_health(dungeon: List[List[int]]) -> int:
    """
    # 174: The demons had captured the princess (P) and imprisoned her in the bottom-right corner of 
    a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was 
    initially positioned in the top-left room and must fight his way through the dungeon to rescue the 
    princess.

    The knight has an initial health point represented by a positive integer. If at any point his health 
    point drops to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering 
    these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health 
    (positive integers).

    In order to reach the princess as quickly as possible, the knight decides to move only rightward or 
    downward in each step.
    """
    M, N = len(dungeon), len(dungeon[0])
    memo = [[0 for _ in range(N)] for _ in range(M)]
    memo[M-1][N-1] = max(1, 1 - dungeon[M-1][N-1])

    for i in range(M-2, -1, -1):
        memo[i][N-1] = max(1, memo[i+1][N-1] - dungeon[i][N-1])
    for j in range(N-2, -1, -1):
        memo[M-1][j] = max(1, memo[M-1][j+1] - dungeon[M-1][j])

    for i in range(M-2, -1, -1):
        for j in range(N-2, -1, -1):
            down = max(1, memo[i+1][j] - dungeon[i][j])
            right = max(1, memo[i][j+1] - dungeon[i][j])
            memo[i][j] = min(right, down)

    return memo[0][0]


if __name__ == "__main__":
    dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    assert calculate_min_health(dungeon) == 3

    print("Passed all tests!")
