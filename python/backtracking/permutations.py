"""
Given a collection of distinct integers, return all possible permutations.
"""
def permutations(nums: list) -> list:
  solutionSet = []
  permuteHelper(nums, solutionSet, 0)
  return solutionSet

def permuteHelper(nums: list, solutionSet: list, start: int) -> None:
  if start == len(nums):
    solutionSet.append(nums.copy())
    return

  for i in range(start, len(nums)):
    nums[start], nums[i] = nums[i], nums[start]
    permuteHelper(nums, solutionSet, start + 1)
    nums[start], nums[i] = nums[i], nums[start]

"""
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.
"""
def permutationsII(nums: list) -> list:
  res = []
  nums.sort()

  def _helper(nums: list, res: list, used: list, temp: list) -> None:
    if len(temp) == len(nums):
      res.append(temp.copy())
      return

    for i in range(len(nums)):
      if (used[i]) or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
        continue
      used[i] = True
      temp.append(nums[i])
      _helper(nums, res, used, temp)
      temp.pop()
      used[i] = False

  _helper(nums, res, [False] * len(nums), [])
  return res

if __name__ == "__main__":
  arr = [1, 2, 3]
  print(permutations(arr))
  arr2 =[1, 1, 2]
  print(permutationsII(arr2))