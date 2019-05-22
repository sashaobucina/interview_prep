from sys import maxsize
"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
"""
def max_subarray(nums: list) -> int:
  max_so_far = -maxsize - 1
  max_ending_here = 0
  for i in range(len(nums)):
    max_ending_here += nums[i]
    if (max_so_far < max_ending_here):
      max_so_far = max_ending_here
    if max_ending_here < 0:
      max_ending_here = 0
  return max_so_far

def max_subarray_dp(nums: list) -> int:
  max_so_far = nums[0]
  curr_max = nums[0]
  for i in range(1, len(nums)):
    curr_max = max(nums[i], curr_max + nums[i])
    max_so_far = max(max_so_far, curr_max)
  return max_so_far

if __name__ == "__main__":
  a = [-13, -3, -15, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
  print(max_subarray_dp(a))