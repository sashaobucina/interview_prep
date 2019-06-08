def is_palindrome(num: int) -> bool:
  # Special cases
  if (num < 0) or (num % 10 == 0 and num != 0):
    return False

  reverted_num = 0
  while num > reverted_num:
    reverted_num = (reverted_num * 10) + (num % 10)
    num = num // 10

  return num == reverted_num or num == reverted_num // 10

def isPalindrome(s: str) -> bool:
  n = len(s) - 1
  i = 0
  while i < n:
    if not s[i].isalnum():
      i += 1
      continue
    if not s[n].isalnum():
      n -= 1
      continue
    if s[i].lower() != s[n].lower():
      print(s[i], s[n])
      return False
    i += 1
    n -= 1
  return True

if __name__ == "__main__":
  print(is_palindrome(123))
  print(isPalindrome("A man, a plan, a canal: Panama"))