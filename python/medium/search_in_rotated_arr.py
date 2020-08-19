from typing import List


def search(nums: List[int], target: int) -> int:
    """
    # 33: Given an integer array nums sorted in ascending order, and an integer target.

    Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You should search for target in nums and if you found return its index, otherwise return -1.
    """
    def find_start_idx(nums) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[0] < nums[-1]:
            return 0
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    
    def bin_search(l, r):
        while l < r:
            mid = l + (r - l) // 2
            
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1

        return l if nums[l] == target else -1
    
    N = len(nums)
    if N == 0:
        return -1
    if N == 1:
        return 0 if target == nums[0] else -1
    
    start_idx = find_start_idx(nums)
    
    if target == nums[start_idx]:
        return start_idx
    if start_idx == 0:
        return bin_search(0, N - 1)
    
    if target < nums[0]:
        return bin_search(start_idx, N - 1)
    
    return bin_search(0, start_idx)


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]

    assert search(nums, 0) == 4
    assert search(nums, 3) == -1
    assert search(nums, 4) == 0
    assert search(nums, 2) == 6

    print("Passed all tests!")