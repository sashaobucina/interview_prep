def two_sum(nums: list, target: int) -> list:
  s = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in s:
      return [s.get(complement), i]
    s[nums[i]] = i
  return None

"""
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
"""
def two_sum_sorted(nums: list, target: int) -> list:
  lo, hi = 0, len(nums) - 1
  while lo < hi:
    sum = nums[lo] + nums[hi]
    if sum == target:
      return [lo, hi]
    if sum < target:
      lo += 1
    else:
      hi -= 1
  return None


if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  print(two_sum(nums, 13))
  print(two_sum_sorted(nums, 18))