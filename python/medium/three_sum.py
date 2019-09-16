def threeSum(nums: list) -> list:
  solutionSet = []
  nums.sort()
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


def three_sum_smaller(nums: list, target: int) -> int:
  counter = 0
  nums.sort()
  for i in range(len(nums) - 1):
    counter += two_sum_smaller(nums, i + 1, target - nums[i])
  return counter

def two_sum_smaller(nums, startInd, target):
  sum = 0
  left = startInd
  right = len(nums) - 1
  while left < right:
    if nums[left] + nums[right] < target:
      sum += right - left
      left += 1
    else:
      right -= 1
  return sum

if __name__ == "__main__":
  arr = [-1, 0, 1, 2, -1, -4]
  print(threeSum(arr))

  arr2 = [-2, -2, 0, 1, 3]
  print(three_sum_smaller(arr2, 2))    # expected: 7