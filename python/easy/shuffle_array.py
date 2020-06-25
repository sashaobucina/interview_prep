from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    """
    # 1470: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    """
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])

    return res


if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    assert shuffle(nums, 3) == [2, 3, 5, 4, 1, 7]

    print("Passed all tests!")
