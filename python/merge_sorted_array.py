def merge_sorted_array(nums1: list, m: int, nums2: list, n: int) -> list:
  while m > 0 or n > 0:
    if m == 0:
      nums1[n-1] = nums2[n-1]
      n -= 1
    elif n == 0 or nums2[n-1] <= nums1[m-1]:
      nums1[m+n-1] = nums1[m-1]
      m -= 1
    else:
      nums1[m+n-1] = nums2[n-1]
      n -= 1


if __name__ == "__main__":
  nums1 = []
  nums2 = [2, 3, 5]
  merge_sorted_array(nums1, 0, [], 0)
  print(nums1)