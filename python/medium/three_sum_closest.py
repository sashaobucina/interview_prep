import sys

"""
Try to find the 3Sum closest to the target.
"""
def threeSumClosest(nums: list, target: int) -> int:
  closestSum = sys.maxsize
  nums.sort()
  minDistance = sys.maxsize
  for i in range(len(nums)):
    j = i + 1
    k = len(nums) - 1
    while j < k:
      distance = abs(target - (nums[i] + nums[j] + nums[k]))
      if distance < minDistance:
        closestSum = nums[i] + nums[j] + nums[k]
        minDistance = distance
        if minDistance == 0:
          return closestSum

      if nums[i] + nums[j] + nums[k] < target:
        j += 1
      else:
        k -= 1

  return closestSum

if __name__ == "__main__":
  arr = [-1, 2, 1, -4]
  print(threeSumClosest(arr, 1))