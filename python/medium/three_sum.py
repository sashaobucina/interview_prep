def threeSum(nums: list) -> list:
  solutionSet = []
  nums = sorted(nums)
  for i in range(len(nums)):
    if i != 0 and nums[i] == nums[i - 1]:
      continue
    j = i + 1
    k = len(nums) - 1
    while j < k:
      if nums[i] + nums[j] + nums[k] == 0:
        solutionSet.append([nums[i], nums[j], nums[k]])
        j += 1
        while j < k and nums[j] == nums[j - 1]:
          j += 1
      elif nums[i] + nums[j] + nums[k] < 0:
        j += 1
      else:
        k -= 1

  return solutionSet

if __name__ == "__main__":
  arr = [-1, 0, 1, 2, -1, -4]
  print(threeSum(arr))