"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
"""
def nextPermutation(nums: list) -> None:
  i = len(nums) - 2
  while i >= 0 and nums[i + 1] <= nums[i]:
    i -= 1
  
  if i >= 0:
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
      j -= 1
    nums[i], nums[j] = nums[j], nums[i]

  # reverse that part of the array
  nums[i+1:] = nums[i+1:][::-1] 

if __name__ == "__main__":
  nums = [1, 1, 5, 4]
  nextPermutation(nums)
  print(nums)