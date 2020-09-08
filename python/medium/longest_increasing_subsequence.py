from typing import List


def lis(nums: List[int]) -> int:
    """
    # 300: Given an unsorted array of integers, find the length of longest increasing subsequence.
    """
    if not nums:
        return 0

    N = len(nums)
    dp = [0] * N

    dp[0] = 1

    ans = 1
    for i in range(1, N):
        curr_max = 0
        for j in range(i):
            if nums[i] > nums[j]:
                curr_max = max(curr_max, dp[j])

        dp[i] = curr_max + 1
        ans = max(ans, dp[i])

    return ans


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    assert lis(arr) == 4

    print("Passed all tests!")
