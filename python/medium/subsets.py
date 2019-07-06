"""
Given a set of distinct integers, return all possible subsets (the power set).

NOTE: Do not return any duplicate subsets
"""
def subsets_I(nums: list) -> list:
  subsets = [[]]
  for el in nums:
    for i in range(len(subsets)):
      currSubset = subsets[i]
      subsets.append(currSubset + [el])

  return subsets

"""
Given a list of integers that may contain duplicates, return all possible subsets (the power set).

NOTE: Do not return any duplicate subsets
"""
def subsets_II(nums: list) -> list:
  if not nums or len(nums) == 0:
    return []

  nums = sorted(nums)
  result = []
  subset = []
  toFindAllSubsets(nums, result, subset, 0)
  return result

def toFindAllSubsets(nums: list, result: list, subset: list, start: int) -> None:
  result.append(subset.copy())
  for i in range(start, len(nums)):
    if (i != start and nums[i] == nums[i - 1]):
      continue
    subset.append(nums[i])
    toFindAllSubsets(nums, result, subset, i + 1)
    subset.pop()


if __name__ == "__main__":
  arr = [1, 2, 3]
  print(subsets_I(arr))
  arr2 = [1, 2, 2]
  print(subsets_II(arr2))