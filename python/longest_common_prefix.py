import sys

def longest_common_prefix(strs: list) -> str:
  if (strs == None or len(strs) == 0): return ""
  for i in range(len(strs[0])):
    c = strs[0][i]
    for j in range(1, len(strs)):
      if (i == len(strs[j]) or strs[j][i] != c):
        return strs[0][0:i]
  return strs[0]

def smallest_len(strs: list) -> int:
  min_len = sys.maxsize
  for i in range(len(strs)):
    if (len(strs[i]) < min_len):
      min_len = len(strs[i])
  return min_len

def is_common_prefix(strs: list, n: int) -> bool:
  str1 = strs[0][0:n]
  for i in range(len(strs)):
    if (not strs[i].startswith(str1)):
      return False
  return True

def lcp_binary_search(strs: list) -> str:
  prefix = ""
  low = 0
  high = smallest_len(strs)
  while (low <= high):
    mid = (low + high) // 2
    if (is_common_prefix(strs, mid)):
      low = mid + 1
    else:
      high = mid - 1
  final_mid = (low + high) // 2
  return strs[0][0:final_mid]

if __name__ == "__main__":
  strs = ["leer", "leet", "lee", "lee", "let"]
  # print(longest_common_prefix(strs))
  print(lcp_binary_search(strs))