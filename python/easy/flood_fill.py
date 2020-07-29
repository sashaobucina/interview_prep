from typing import List
from collections import deque


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    """
    # 733: An image is represented by a 2-D array of integers, each integer representing the pixel value 
    of the image (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
    and a pixel value newColor, "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
    to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally 
    to those pixels (also with the same color as the starting pixel), and so on. Replace the color of 
    all of the aforementioned pixels with the newColor.

    At the end, return the modified image.

    This sol'n uses an iterative BFS approach w/ a queue.
    """
    old_color = image[sr][sc]
    if old_color == new_color:
        return image

    m, n = len(image), len(image[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q = deque([(sr, sc)])
    while q:
        x, y = q.pop()
        image[x][y] = new_color

        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if (0 <= x2 < m) and (0 <= y2 < n) and (image[x2][y2] == old_color):
                q.appendleft((x2, y2))

    return image


def flood_fill_dfs(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    """
    This sol'n uses a recursive DFS approach.
    """
    def dfs(x: int, y: int):
        if image[x][y] == color:
            image[x][y] = new_color

            if x > 0:
                dfs(x - 1, y)
            if y > 0:
                dfs(x, y - 1)
            if x < m - 1:
                dfs(x + 1, y)
            if y < n - 1:
                dfs(x, y + 1)

    color = image[sr][sc]
    m, n = len(image), len(image[0])

    if color != new_color:
        dfs(sr, sc)

    return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert flood_fill_dfs(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    image = [[0, 0, 0], [0, 1, 1]]
    assert flood_fill(image, 1, 1, 1) == image
    assert flood_fill_dfs(image, 1, 1, 1) == image

    print("Passed all tests!")
