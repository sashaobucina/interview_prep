from typing import List


def matrix_reshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    # 566: In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into 
    a new one with different size but keep its original data.

    You're given a matrix represented by a two-dimensional array, and two positive integers r and c 
    representing the row number and column number of the wanted reshaped matrix, respectively.

    The reshaped matrix need to be filled with all the elements of the original matrix in the same 
    row-traversing order as they were.

    If the 'reshape' operation with given parameters is possible and legal, output the new reshaped 
    matrix; Otherwise, output the original matrix.
    """
    R, C = len(nums), len(nums[0])
    if not nums or (R * C) != (r * c):
        return nums

    count = 0
    res = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(R):
        for j in range(C):
            res[count // c][count % c] = nums[i][j]
            count += 1

    return res


if __name__ == "__main__":
    nums = [[1, 2], [3, 4]]
    assert matrix_reshape(nums, 1, 4) == [[1, 2, 3, 4]]

    nums = [[1, 2], [3, 4]]
    assert matrix_reshape(nums, 2, 4) == nums

    print("Passed all tests!")
