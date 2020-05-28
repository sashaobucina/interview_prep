from typing import List


def valid_sudoku(board: List[List[str]]) -> bool:
    """
    # 36: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
    """
    if not board or len(board) != len(board[0]):
        return False

    for idx in range(len(board)):
        if not (_validate_row(board, row=idx) and _validate_col(board, col=idx)
                and _validate_box(board, box=idx)):
            return False
    return True


def _validate_row(board: List[List[int]], row: int) -> bool:
    s = set()

    for val in board[row]:
        if val == ".":
            continue
        if val in s:
            return False
        s.add(val)

    return True


def _validate_col(board: List[List[int]], col: int) -> bool:
    s = set()

    for row in range(len(board)):
        curr_val = board[row][col]
        if curr_val == ".":
            continue
        if curr_val in s:
            return False
        s.add(curr_val)

    return True


def _validate_box(board: List[List[int]], box: int) -> bool:
    s = set()
    row = 3 * (box // 3)
    col = 3 * (box % 3)

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            val = board[i][j]
            if val == ".":
                continue
            if val in s:
                return False
            s.add(val)

    return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert valid_sudoku(board)

    print("Passed all tests!")
