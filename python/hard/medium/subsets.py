import copy

def subsets_II(nums: list) -> list:
  if not nums or len(nums) == 0:
    return []

  nums = sorted(nums)
  result = []
  subset = []
  toFindAllSubsets(nums, result, subset, 0)
  return result

def toFindAllSubsets(nums: list, result: list, subset: list, start: int) -> None:
  result.append(copy.deepcopy(subset))
  for i in range(start, len(nums)):
    if (i != start and nums[i] == nums[i - 1]):
      continue
    subset.append(nums[i])
    toFindAllSubsets(nums, result, subset, i + 1)
    subset.pop()


if __name__ == "__main__":
  arr = [1, 2, 2]
  print(subsets_II(arr))