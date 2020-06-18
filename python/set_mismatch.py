from typing import List


def find_error(nums: List[int]) -> List[int]:
    """
    # 645: The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, 
    one of the numbers in the set got duplicated to another number in the set, which results in 
    repetition of one number and loss of another number.

    Given an array nums representing the data status of this set after the error. 
    Your task is to firstly find the number occurs twice and then find the number that is missing. 
    Return them in the form of an array.
    """
    cnt = [0] * len(nums)
    for num in nums:
        cnt[num - 1] += 1

    dup, missing = -1, 1
    for i in range(len(cnt)):
        if cnt[i] == 0:
            missing = i + 1
        elif cnt[i] == 2:
            dup = i + 1

    return [dup, missing]


def find_error_alt(nums: List[int]) -> List[int]:
    """
    This solution uses constant memory.
    """
    dup, missing = -1, 1
    for num in nums:
        if nums[abs(num) - 1] < 0:
            dup = abs(num)
        else:
            nums[abs(num) - 1] *= -1

    for i in range(1, len(nums)):
        if nums[i] > 0:
            missing = i + 1

    return [dup, missing]


if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    assert find_error(nums) == [2, 3]
    assert find_error_alt(nums) == [2, 3]

    print("Passed all tests!")
