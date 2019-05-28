def is_palindrome(num: int) -> bool:
  # Special cases
  if (num < 0) or (num % 10 == 0 and num != 0):
    return False

  reverted_num = 0
  while num > reverted_num:
    reverted_num = (reverted_num * 10) + (num % 10)
    num = num // 10

  print(reverted_num, num)
  return num == reverted_num or num == reverted_num // 10

if __name__ == "__main__":
  print(is_palindrome(123))