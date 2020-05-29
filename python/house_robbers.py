from typing import List


def rob_dp(arr: List[int]) -> int:
    """
    # 198: You are a professional robber planning to rob houses along a street. 
    # Each house has a certain amount of money stashed, the only constraint stopping you from robbing 
    # each of them is that adjacent houses have security system connected and it will automatically 
    # contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, 
    determine the maximum amount of money you can rob tonight without alerting the police.
    """
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[n-1]


def rob(arr: List[int]) -> int:
    even = odd = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even += arr[i]
            even = even if even > odd else odd
        else:
            odd += arr[i]
            odd = odd if odd > even else even

    return max(even, odd)


if __name__ == "__main__":
    arr = [122, 23, 45, 122]
    assert rob(arr) == 244
    assert rob_dp(arr) == 244

    arr = [2, 1]
    assert rob(arr) == 2
    assert rob_dp(arr) == 2

    print("Passed all tests!")
