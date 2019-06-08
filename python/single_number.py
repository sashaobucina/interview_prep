"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
def singleNumber(nums: list) -> int:
  return 2 * sum(set(nums)) - sum(nums)

def singleNumberXOR(nums: list) -> int:
  a = 0
  for i in nums:
    a ^= i
  return a

if __name__ == "__main__":
  arr = [2, 2, 4, 1, 1]
  print(singleNumber(arr))
  print(singleNumberXOR(arr))