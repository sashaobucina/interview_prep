"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

""" Divide and conquer approach """
def majorityElementDC(nums: list) -> int:
  return _majorityElementRec(nums, 0, len(nums) - 1)

def _majorityElementRec(nums: list, lo: int, hi: int):
  if lo == hi:
    return nums[lo]
  
  mid = (hi-lo) // 2 + lo
  left = _majorityElementRec(nums, lo, mid)
  right = _majorityElementRec(nums, lo+1, hi)

  if left == right:
    return left

  right_count, left_count = 0, 0
  for i in range(lo, hi + 1):
    if nums[i] == left:
      left_count += 1
    elif nums[i] == right:
      right_count += 1
  return left if left_count > right_count else right

""" Boyer-Moore voting algorithm"""
def majorityElementVoting(nums: list) -> int:
  count = 0
  candidate = None
  for num in nums:
    if count == 0:
      candidate = num
    count += 1 if num == candidate else -1
  return candidate

if __name__ == "__main__":
  nums = [3, 2, 3]
  print(majorityElementDC(nums))
  print(majorityElementVoting(nums))