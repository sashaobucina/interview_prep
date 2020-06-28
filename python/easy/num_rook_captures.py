from itertools import product
from typing import List


def num_rook_captures(board: List[List[str]]) -> int:
    """
    # 999: On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, 
    and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. 
    Uppercase characters represent white pieces, and lowercase characters represent black pieces.

    The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, 
    west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, 
    or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot 
    move into the same square as other friendly bishops.

    Return the number of pawns the rook can capture in one move.
    """
    rook = None
    for i, j in product(range(8), range(8)):
        if board[i][j] == "R":
            rook = (i, j)
            break

    captures = 0
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = rook
        x, y = x + dx, y + dy

        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == "p":
                captures += 1
                break
            elif board[x][y] == "B":
                break

            x, y = x + dx, y + dy

    return captures


if __name__ == "__main__":
    board = [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]
            ]
    assert num_rook_captures(board) == 3

    print("Passed all tests!")
