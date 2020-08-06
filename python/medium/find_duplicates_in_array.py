from typing import List


def find_duplicates_naive(nums: List[int]) -> List[int]:
    """
    # 442: Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?

    Time complexity: O(n)
    Space complexity: O(n)
    """
    ans = []
    visited = set()
    for num in nums:
        if num in visited:
            ans.append(num)
        else:
            visited.add(num)

    return ans


def find_duplicates(nums: List[int]) -> List[int]:
    """
    This solution uses the fact of that the integers in the input array arr satisfy 1 ≤ arr[i] ≤ n, 
    where n is the size of array as a supplement.

    This presents us with two key insights:
        - All the integers present in the array are positive. i.e. arr[i] > 0 for any valid index i. 3
        - The decrement of any integers present in the array must be an accessible index in the array. 
            i.e. for any integer x in the array, x-1 is a valid index, and thus, arr[x-1] is a valid 
            reference to an element in the array. 4

    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(nums)):
        nums[abs(nums[i]) - 1] *= -1

    ans = []
    for i, num in enumerate(nums):
        if nums[abs(num) - 1] > 0:
            ans.append(abs(num))
            nums[abs(num) - 1] *= -1

    return ans


def find_duplicates_better(nums: List[int]) -> List[int]:
    """
    Same algorithm as above, but done in a single pass.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    ans = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            ans.append(abs(num))
        nums[abs(num) - 1] *= -1

    return ans


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    assert find_duplicates_naive(nums[:]) in [[2, 3], [3, 2]]
    assert find_duplicates(nums[:]) in [[2, 3], [3, 2]]
    assert find_duplicates_better(nums[:]) in [[2, 3], [3, 2]]

    print("Passed all tests!")
