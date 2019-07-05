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

if __name__ == "__main__":
  arr = [1, 2, 3]
  print(permutations(arr))