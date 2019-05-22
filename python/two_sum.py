def two_sum(nums: list, target: int) -> list:
  s = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in s:
      return [s.get(complement), i]
    s[nums[i]] = i
  return None


if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  print(two_sum(nums, 13))