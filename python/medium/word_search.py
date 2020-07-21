from typing import List


def word_search(board: List[List[int]], word: str) -> bool:
    """
    # 79: Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are 
    those horizontally or vertically neighboring. The same letter cell may not be used more than once.

    This sol'n uses backtracking (DFS) to search for the word.
    """
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(word, x, y):
        if word == "":
            return True

        ret_val = False
        if 0 <= x < m and 0 <= y < n:
            ch, rest = word[0], word[1:]
            if board[x][y] != ch:
                return False

            board[x][y] = "#"
            for dx, dy in directions:
                if dfs(rest, x + dx, y + dy):
                    ret_val = True
                    break

            board[x][y] = ch

        return ret_val

    for i in range(m):
        for j in range(n):
            if dfs(word, i, j):
                return True

    return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert word_search(board, "ABCCED")
    assert word_search(board, "SEE")
    assert not word_search(board, "ABCB")

    print("Passed all tests!")
