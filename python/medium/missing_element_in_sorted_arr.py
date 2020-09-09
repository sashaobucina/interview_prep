from typing import List


def missing_element(nums: List[int], k: int) -> int:
    """
    # 1060: Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost 
    number of the array.
    """
    def missing(idx):
        return nums[idx] - nums[0] - idx

    N = len(nums)
    if missing(N - 1) < k:
        return nums[N - 1] + k - missing(N - 1)

    l, r = 0, N - 1
    while l < r:
        mid = l + (r - l) // 2

        if missing(mid) < k:
            l = mid + 1
        else:
            r = mid

    return nums[l - 1] + k - missing(l - 1)


if __name__ == "__main__":
    nums = [4, 7, 9, 10]
    assert missing_element(nums, 1) == 5

    nums = [4, 7, 9, 10]
    assert missing_element(nums, 3) == 8

    nums = [1, 2, 4]
    assert missing_element(nums, 3) == 6

    print("Passed all tests!")
