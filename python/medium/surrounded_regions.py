from typing import List
from collections import deque


def solve(board: List[List[int]]) -> None:
    """
    # 130: Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    EXPLANATION:
        - Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
        are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the 
        border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected 
        horizontally or vertically.
    """
    if not board or not board[0]:
        return

    M, N = len(board), len(board[0])

    if M <= 2 or N <= 2:
        return

    q = deque([])

    for i in range(M):
        q.appendleft((i, 0))
        q.appendleft((i, M - 1))

    for i in range(1, N - 1):
        q.appendleft((0, i))
        q.appendleft((N - 1, i))

    while q:
        x, y = q.pop()
        if 0 <= x < M and 0 <= y < N and board[x][y] == "O":
            board[x][y] = "N"
            for pos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                q.appendleft(pos)

    for x in range(M):
        for y in range(N):
            if board[x][y] == "N":
                board[x][y] = "O"
            else:
                board[x][y] = "X"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected_board = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    solve(board)
    assert board == expected_board

    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    expected_board = [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    solve(board)
    assert board == expected_board

    print("Passed all tests!")
