from typing import List


def sum_subarray_mins(A: List[int]) -> int:
    """
    # 907: Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

    Since the answer may be large, return the answer modulo 10^9 + 7.

    This solution keeps track of two monotonic stacks for previous less element and next less element.
    Also, left and right lists are kept to track the disatances between for the PLE and NLE for each element in A.
        - For an index i, res += A[i] * left[i] * right[i]

    More detailed explanation:
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
    """
    in_stk_p, in_stk_n = [], []

    # left is for the distance to previous less element
    left = list(range(1, len(A) + 1))

    # right is for the distance to next less element
    right = list(range(len(A), 0, -1))

    for i in range(len(A)):
        # previous less (PLE)
        while in_stk_p and A[in_stk_p[-1]] > A[i]:
            in_stk_p.pop()

        left[i] = i + 1 if not in_stk_p else (i - in_stk_p[-1])
        in_stk_p.append(i)

        # next less (NLE)
        while in_stk_n and A[in_stk_n[-1]] > A[i]:
            x = in_stk_n.pop()
            right[x] = i - x

        in_stk_n.append(i)

    res = 0
    for i in range(len(A)):
        res = (res + A[i] * left[i] * right[i]) % (10**9 + 7)

    return res


if __name__ == "__main__":
    A = [3, 1, 2, 4]
    assert sum_subarray_mins(A) == 17

    print("Passed all tests!")
