from typing import List


def game_of_life(board: List[List[int]]) -> None:
    """
    # 289: According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a 
    cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell 
    interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four 
    rules (taken from the above Wikipedia article):
        - Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by over-population..
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Write a function to compute the next state (after one update) of the board given its current state. 
    The next state is created by applying the above rules simultaneously to every cell in the current state, 
    where births and deaths occur simultaneously.
    """
    R, C = len(board), len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (1, 1), (1, -1), (-1, 1)]

    def _sum_neighbors(row: int, col: int) -> int:
        alive = 0
        for dr, dc in dirs:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < R and 0 <= new_col < C:
                if board[new_row][new_col] > 0:
                    alive += 1

        return alive

    for r in range(R):
        for c in range(C):
            alive = _sum_neighbors(r, c)
            if board[r][c] > 0 and (alive < 2 or alive > 3):
                board[r][c] = 2
            elif board[r][c] <= 0 and alive == 3:
                board[r][c] = -1

    for r in range(R):
        for c in range(C):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == -1:
                board[r][c] = 1


if __name__ == "__main__":
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    expected = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]
    game_of_life(board)
    assert board == expected

    print("Passed all tests!")
