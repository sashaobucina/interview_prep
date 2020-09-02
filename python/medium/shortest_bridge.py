from typing import List
from collections import deque


def shortest_bridge(A: List[List[int]]) -> int:
    """
    # 934: In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected 
    group of 1s not connected to any other 1s.)

    Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

    Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
    """
    R, C = len(A), len(A[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # define DFS search of groups
    def dfs(row, col, group):
        A[row][col] = marker
        group.append((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < R) and (0 <= new_col < C) and (A[new_row][new_col] == 1):
                dfs(new_row, new_col, group)

        return group

    # use DFS to find the two groups, mark them differently and store them in groups list
    groups, marker = [], 2
    for r in range(R):
        for c in range(C):
            if A[r][c] == 1:
                groups.append((dfs(r, c, []), marker))
                marker += 1

    # construct queue from smaller source group & target set
    groups = sorted(groups, key=lambda x: len(x[0]))

    src_group, src_marker = groups[0]
    q = deque([(row, col, 0) for row, col in src_group])

    target = set(groups[1][0])

    # perform BFS until found the other group marker, ensures shortest path
    while q:
        row, col, curr_distance = q.pop()

        if (row, col) in target:
            return curr_distance - 1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < R and 0 <= new_col < C and A[new_row][new_col] != src_marker:
                q.appendleft((new_row, new_col, curr_distance + 1))
                A[new_row][new_col] = src_marker

    # should never reach here if two groups in A
    return -1


if __name__ == "__main__":
    A = [[0, 1], [1, 0]]
    assert shortest_bridge(A) == 1

    A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    assert shortest_bridge(A) == 2

    A = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    assert shortest_bridge(A) == 1

    print("Passed all tests!")
