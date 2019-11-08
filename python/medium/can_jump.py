from typing import List

def canJump(nums: List[int]) -> bool:
  """Given an array of non-negative integers, you are initially positioned at 
  the first index of the array.

  Each element in the array represents your maximum jump length at that position.

  Determine if you are able to reach the last index.

  NOTE: Greedy solution implemented, O(n) time complexity, O(1) space complexity
  """
  i, furthest =  0, 0
  while i <= furthest and i < len(nums):
    furthest = max(furthest, i + nums[i])
    i += 1

  return furthest >= len(nums) - 1

if __name__ == "__main__":
  print(canJump([1,5,2,1,0,2,0]))
  # expected: True

  print(canJump([3,2,1,0,4]))
  # expected: False