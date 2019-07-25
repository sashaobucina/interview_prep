def fourSum(nums: list, target: int) -> list:
  solutionSet = []

  for i in range(len(nums)):
    if i != 0 and nums[i] == nums[i - 1]:
      continue

    for j in range(i + 1, len(nums)):
      if j != i + 1 and nums[j] == nums[j - 1]:
        continue

      k, l = j + 1, len(nums) - 1

      while k < l:
        if nums[i] + nums[j] + nums[k] + nums[l] == target:
          solutionSet.append([nums[i], nums[j], nums[k], nums[l]])
          k += 1
          while k < l and nums[k] == nums[k - 1]:
            k += 1
        elif nums[i] + nums[j] + nums[k] + nums[l] < target:
          k += 1
        else:
          l -= 1

  return solutionSet

if __name__ == "__main__":
  arr = [1, 0, -1, 0, -2, 2]
  print(fourSum(arr, 0))

  arr = [0, 0, 0, 0]
  print(fourSum(arr, 0))