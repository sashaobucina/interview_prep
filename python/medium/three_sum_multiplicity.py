from typing import List
from collections import Counter


def three_sum_multi(A: List[int], target: int) -> int:
    """
    # 923: Given an integer array A, and an integer target, return the number of tuples i, j, k 
    such that i < j < k and A[i] + A[j] + A[k] == target.

    As the answer can be very large, return it modulo 10^9 + 7.
    """
    ans, MOD = 0, 10**9 + 7
    counted = Counter(A)
    keys = sorted(counted)
    
    for i, x in enumerate(keys):
        complement = target - x
        lo, hi = i, len(keys) - 1
        
        while lo <= hi:
            y, z = keys[lo], keys[hi]

            if y + z < complement:
                lo += 1
            elif y + z > complement:
                hi -= 1
            else:
                if i < lo < hi:
                    ans += counted[x] * counted[y] * counted[z]
                elif i == lo < hi:
                    ans += counted[x] * (counted[x] - 1) // 2 * counted[z]
                elif i < lo == hi:
                    ans += counted[x] * counted[y] * (counted[y] - 1) // 2
                else:
                    ans += counted[x] * (counted[x] - 1) * (counted[x] - 2) // 6
                    
                lo += 1
                hi -= 1
                
    return ans % MOD


if __name__ == "__main__":
    A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert three_sum_multi(A, target=8) == 20

    A = [1, 1, 2, 2, 2, 2]
    assert three_sum_multi(A, target=5) == 12

    print("Passed all tests!")
