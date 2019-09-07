"""
Given a sorted integer array nums, where the range of elements are in the 
inclusive range [lower, upper], return its missing ranges.
"""
def missing_range(nums: list, lower: int, upper: int) -> list:
  output = []
  nums = [lower - 1] + nums + [upper + 1]
  for num1, num2 in zip(nums, nums[1:]):
    if num1 + 2 == num2:
      output.append(str(num1 + 1))
    elif num1 + 2 < num2:
      output.append("{0}->{1}".format(num1 + 1, num2 - 1))
  return output

def missing_range_alt(nums, lower, upper):
  output = []
  nums = [lower - 1] + nums + [upper + 1]
  for i in range(len(nums) - 1):
    if nums[i] + 2 == nums[i + 1]:
      output.append(str(nums[i] + 1))
    elif nums[i] + 2 < nums[i + 1]:
      output.append("{0}->{1}".format(nums[i] + 1, nums[i + 1] - 1))

  return output

if __name__ == "__main__":
  nums = [0,1,3,50,75]
  print(missing_range(nums, 0, 99))   # expected: ['2', '4->49', '51->74', '76->99']
  print(missing_range_alt(nums, 0, 99))