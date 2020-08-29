from typing import List


def pancake_sort(A: List[int]) -> List[int]:
    """
    # 969: Given an array of integers A, We need to sort the array performing a series of pancake flips.

    In one pancake flip we do the following steps:
        - Choose an integer k where 0 <= k < A.length.
        - Reverse the sub-array A[0...k].

    For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the 
    sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

    Return an array of the k-values of the pancake flips that should be performed in order to sort A. 
    Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.
    """
    def flip(sublist, k):
        i = 0
        while i < k / 2:
            sublist[i], sublist[k - i - 1] = sublist[k - i - 1], sublist[i]
            i += 1

    ans = []
    val = len(A)

    while val > 0:
        # find next to sort
        idx = A.index(val)

        if idx != val - 1:
            if idx != 0:
                ans.append(idx + 1)
                flip(A, idx + 1)

            # now that at head, flip it to the back
            ans.append(val)
            flip(A, val)

        val -= 1

    return ans


if __name__ == "__main__":
    A = [3, 2, 4, 1]
    flips = pancake_sort(A)

    assert A == [1, 2, 3, 4]
    assert len(flips) < 10 * len(A)

    print("Passed all tests!")
