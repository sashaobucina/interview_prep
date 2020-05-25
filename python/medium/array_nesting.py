
import sys
from typing import List

MAX_INT = sys.maxsize


def array_nesting(nums: List[int]) -> int:
    """
    A zero-indexed array A of length N contains all integers from 0 to N-1. 
    Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } 
    subjected to the rule below.

    Suppose the first element in S starts with the selection of element A[i] of index = i, 
    the next element in S should be A[A[i]], and then A[A[A[i]]]… 
    By that analogy, we stop adding right before a duplicate element occurs in S.
    """
    longest = 0
    for i in range(len(nums)):
        if nums[i] != MAX_INT:
            start = nums[i]
            count = 0

            while nums[start] != MAX_INT:
                tmp = start
                start = nums[start]
                nums[tmp] = MAX_INT
                count += 1

            longest = max(longest, count)

    return longest


if __name__ == "__main__":
    l = [5, 4, 0, 3, 1, 6, 2]
    print(array_nesting(l))     # Expected: 4

    l = [0, 1, 2]
    print(array_nesting(l))     # Expected: 1
