import heapq
from typing import List


def trap_rain_water(height_map: List[List[int]]) -> int:
    """
    # 407: Given an m x n matrix of positive integers representing the height of each unit cell in a 2D 
    elevation map, compute the volume of water it is able to trap after raining.

    Visualization: https://www.youtube.com/watch?v=cJayBq38VYw
    """
    m, n = len(height_map), len(height_map[0])
    visited = set()

    hq = []
    for i in range(m):
        for j in range(n):
            if i in (0, m - 1) or j in (0, n - 1):
                heapq.heappush(hq, (height_map[i][j], i, j))
                visited.add((i, j))

    trapped = 0
    while hq:
        # curr_height maintains the leak point at that current time
        curr_height, i, j = heapq.heappop(hq)

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < m and 0 <= j2 < n and (i2, j2) not in visited:
                trapped += max(0, curr_height - height_map[i2][j2])
                heapq.heappush(
                    hq, (max(curr_height, height_map[i2][j2]), i2, j2))
                visited.add((i2, j2))

    return trapped


if __name__ == "__main__":
    height_map = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    assert trap_rain_water(height_map) == 4

    print("Passed all tests!")
