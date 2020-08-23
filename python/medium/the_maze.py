from typing import List
from collections import deque


def has_path(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """
    # 490: There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, 
    down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could 
    choose the next direction.

    Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

    The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.

    You may assume that the borders of the maze are all walls.
    The start and destination coordinates are represented by row and column indexes.
    """
    m, n = len(maze), len(maze[0])

    start_x, start_y = start
    dest_x, dest_y = destination

    visited = {(start_x, start_y)}
    q = deque([(start_x, start_y)])
    while q:
        x, y = q.pop()

        if x == dest_x and y == dest_y:
            return True

        # check where next wall is for each direction
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            _x, _y = x, y
            while (0 <= _x + dx < m) and (0 <= _y + dy < n) and (maze[_x + dx][_y + dy] != 1):
                _x += dx
                _y += dy

            if (_x, _y) not in visited:
                q.appendleft((_x, _y))
                visited.add((_x, _y))

    return False


if __name__ == "__main__":
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start, destination = [0, 4], [4, 4]
    assert has_path(maze, start, destination)

    start, destination = [0, 4], [3, 2]
    assert not has_path(maze, start, destination)

    print("Passed all tests!")
