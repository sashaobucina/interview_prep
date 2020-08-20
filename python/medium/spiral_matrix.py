from typing import List


def spiral_order(matrix: List[List[int]]) -> List[List[int]]:
    """
    # 54: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    """
    if not matrix:
        return []

    ans = []

    R, C = len(matrix), len(matrix[0])
    seen = [[False for _ in range(C)] for _ in range(R)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    row, col, dir_idx = 0, 0, 0
    for _ in range(R * C):
        ans.append(matrix[row][col])
        seen[row][col] = True

        next_row, next_col = row + dr[dir_idx], col + dc[dir_idx]
        if 0 <= next_row < R and 0 <= next_col < C and not seen[next_row][next_col]:
            row, col = next_row, next_col
        else:
            dir_idx = (dir_idx + 1) % 4
            row, col = row + dr[dir_idx], col + dc[dir_idx]

    return ans


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    print("Passed all tests!")
