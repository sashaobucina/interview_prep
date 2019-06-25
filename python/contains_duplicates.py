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


if __name__ == "__main__":
  arr = [1, 2, 3, 1]
  print(contains_duplicate(arr))

  arr2 = [1, 2, 3, 1, 4, 1]
  print(contains_duplicate_II(arr2, 10))