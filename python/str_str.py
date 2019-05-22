def str_str(haystack: str, needle: str) -> int:
  i = 0
  while i <= len(haystack) - len(needle):
    if (haystack[i:i+len(needle)] == needle):
      return i
    i+=1
  return -1


if __name__ == "__main__":
  print(str_str("", "ll"))
  print(str_str("aaaaaa", "bba"))