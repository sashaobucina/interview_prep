"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.

NOTE: This solution is in O(n) time and is not optimized
"""
def findMedianSortedArraysBad(nums1: list, nums2: list) -> float:
  nums3 = []
  i, j, m, n = 0, 0, len(nums1), len(nums2)

  while i < m and j < n:
    if nums1[i] < nums2[j]:
      nums3.append(nums1[i])
      i += 1
    else:
      nums3.append(nums2[j])
      j += 1

  while i < m:
    nums3.append(nums1[i])
    i += 1
  while j < n:
    nums3.append(nums2[j])
    j += 1

  totalLen = len(nums3)
  if totalLen % 2 != 0:
    return float(nums3[totalLen // 2])
  else:
    return (nums3[totalLen // 2 - 1] + nums3[totalLen // 2]) / 2

if __name__ == "__main__":
  nums1, nums2 = [1, 3, 5, 8, 9, 10], [2, 4, 6, 7, 11, 14]
  print(findMedianSortedArraysBad(nums1, nums2))   # expected value - 6.5