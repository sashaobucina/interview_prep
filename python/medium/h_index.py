from typing import List


def h_index_II(citations: List[int]) -> int:
    """
    # 274: Given an array of citations sorted in ascending order (each citation is a non-negative integer) 
    # of a researcher, write a function to compute the researcher's h-index.

    According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N 
    papers have at least h citations each, and the other N − h papers have no more than h citations each."

    EXAMPLE:
    Input: citations = [0,1,3,5,6]
    Output: 3
    Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
        received 0, 1, 3, 5, 6 citations respectively. 
        Since the researcher has 3 papers with at least 3 citations each and the remaining 
        two with no more than 3 citations each, her h-index is 3.

    NOTE:
    If there are several possible values for h, the maximum one is taken as the h-index.

    Follow up:
        - This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
        - Could you solve it in logarithmic time complexity?

    This sol'n has a runtime complexity of O(logn).
    """
    N = len(citations)
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2

        if citations[mid] < N - mid:
            l = mid + 1
        else:
            r = mid - 1

    return N - l


def h_index_II_linear(citations: List[int]) -> int:
    """
    This sol'n has a runtime complexity of O(n).
    """
    N = len(citations)
    i = N - 1

    while i >= 0:
        if citations[i] <= N - i:
            break
        i -= 1

    return N - i - 1


if __name__ == "__main__":
    citations = [0, 1, 2, 4, 5, 8, 10, 13]
    assert h_index_II_linear(citations) == h_index_II(citations) == 4

    print("Passed all tests!")
