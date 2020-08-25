def min_domino_rotations(A: list, B: list) -> int:
    """
    # 1007: In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th 
    domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

    We may rotate the i-th domino, so that A[i] and B[i] swap values.

    Return the minimum number of rotations so that all the values in A are the same, 
    or all the values in B are the same.

    If it cannot be done, return -1.
    """
    def check(target: int) -> int:
        rotations_a, rotations_b = 0, 0

        for i in range(len(A)):
            if A[i] != target and B[i] != target:
                return -1
            elif A[i] != target:
                rotations_a += 1
            elif B[i] != target:
                rotations_b += 1

        return min(rotations_a, rotations_b)

    res = check(A[0])
    if res != -1 or A[0] == B[0]:
        return res

    return check(B[0])


if __name__ == "__main__":
    A, B = [2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]
    assert min_domino_rotations(A, B) == 2

    A, B = [3, 5, 1, 2, 3], [3, 6, 3, 3, 4]
    assert min_domino_rotations(A, B) == -1

    print("Passed all tests!")
