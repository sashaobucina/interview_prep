from typing import List


def find_max_length(nums: List[int]) -> int:
    """
    # 525: Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

    This solution produces a TLE!

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    total = 0
    for i in range(len(nums)):
        cnt, equal = 0, 0
        for j in range(i, len(nums)):
            if nums[j] == 1:
                equal += 1
            else:
                equal -= 1

            cnt += 1
            if equal == 0:
                total = max(total, cnt)

    return total


def find_max_length_extra_arr(nums: List[int]) -> int:
    """
    This solution uses an extra array to reduce time complexity to be linear.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    N = len(nums)
    count, max_len = 0, 0
    memo = [-2] * (2 * N + 1)
    memo[N] = -1

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if memo[count + N] >= -1:
            max_len = max(max_len, i - memo[count + N])
        else:
            memo[count + N] = i

    return max_len


def find_max_length_hash_map(nums: List[int]) -> int:
    """
    This solution uses a hash map to achieve more efficient space.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    d = {0: -1}
    count, max_len = 0, 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count not in d:
            d[count] = i
        else:
            max_len = max(max_len, i - d[count])

    return max_len


if __name__ == "__main__":
    nums = [0, 1]
    assert find_max_length(nums) == find_max_length_hash_map(
        nums) == find_max_length_extra_arr(nums) == 2

    nums = [0, 1, 1]
    assert find_max_length(nums) == find_max_length_hash_map(
        nums) == find_max_length_extra_arr(nums) == 2

    nums = [0, 0, 1, 0, 0, 1, 1, 0, 0]
    assert find_max_length(nums) == find_max_length_hash_map(
        nums) == find_max_length_extra_arr(nums) == 6

    print("Passed all tests!")
