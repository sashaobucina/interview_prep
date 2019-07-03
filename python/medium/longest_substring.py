"""
Longest substring with no repeating characters. Sliding window approach
"""
def longestSubstring(s: str) -> int:
  charMap = {}
  ans, i, j = 0, 0, 0
  while j < len(s):
    if s[j] in charMap:
      i = max(charMap[s[j]], i)
    ans = max(ans, j - i + 1)
    charMap[s[j]] = j + 1
    j += 1

  return ans

if __name__ == "__main__":
  print(longestSubstring("abcabcbb"))