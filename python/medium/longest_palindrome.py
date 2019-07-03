def longest_palindrome(s: str) -> str:
  if not s or len(s) < 1:
    return ""

  start, end = 0, 0
  for i in range(len(s)):
    len1 = expandFromCenter(s, i, i)
    len2 = expandFromCenter(s, i, i + 1)
    maxLen = max(len1, len2)
    if maxLen > end - start:
      start = i - (maxLen - 1) // 2
      end = i + maxLen // 2

  return s[start: end + 1]


def expandFromCenter(s: str, left: int, right: int) -> int:
  L, R = left, right
  while L >= 0 and R < len(s) and s[L] == s[R]:
    L -= 1
    R += 1
  return R - L - 1

if __name__ == "__main__":
  print(longest_palindrome("heracecarls"))