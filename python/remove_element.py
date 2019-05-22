def remove_element(nums: list, val: int) -> int:
  i = 0
  while i < len(nums):
    if (nums[i] == val):
      del nums[i]
    else:
      i+=1
  return i

### Two pointers approach ###
def remove_element_ptrs(nums: list, val: int) -> int:
  i = 0
  n = len(nums)
  while i < n:
    if (nums[i] == val):
      nums[i] = nums[n-1]
      n-=1
    else:
      i+=1
  return n

if __name__ == "__main__":
  nums = [0, 1, 2, 2, 3, 0, 4, 2]
  print(remove_element_ptrs(nums, 2))