""" Returns true if duplicate present, false otherwise. """
def contains_duplicate(nums: list) -> bool:
  s = set(nums)
  return len(nums) != len(s)

"""
Returns true if duplicate present and absolute distance between indices within k, 
otherwise returns False.
"""
def contains_duplicate_II(nums: list, k: int) -> bool:
  tracker = {}
  for i in range(len(nums)):
    if nums[i] in tracker and abs(i - tracker[nums[i]]) <= k:
      return True
    tracker[nums[i]] = i
  return False

"""
Returns true if duplicate present, absolute distance between indices within k, and 
absolute difference between values is within t, otherwise returns false.
NOTE: Bucket solution - O(n) runtime
"""
def contains_duplicate_III(nums: list, k: int, t: int) -> bool:
  if len(nums) < 2 or k < 0 or t < 0:
    return False
  buckets = {}
  width = t + 1
  for i, num in enumerate(nums):
    buck = num // width
    if buck in buckets:
      return True
    else:
      buckets[buck] = num
      if buck - 1 in buckets and num - buckets[buck - 1] <= t:
        return True
      if buck + 1 in buckets and buckets[buck + 1] - num <= t:
        return True
      if i >= k:
        del buckets[nums[i - k] // width]
  return False

if __name__ == "__main__":
  arr = [1, 2, 3, 1]
  print(contains_duplicate(arr))

  arr2 = [1, 2, 3, 1, 4, 1]
  print(contains_duplicate_II(arr2, 10))

  arr3 = [1, 5, 9, 1, 5, 9]
  print(contains_duplicate_III(arr3, 2, 3))