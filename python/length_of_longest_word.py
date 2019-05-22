def length_of_last_word(s: str) -> int:
  n = 0
  for i in reversed(range(len(s))):
    if (n != 0 and s[i] == " "):
      return n
    elif (s[i] != " "):
      n+=1
  return n

def length_of_last_word_opt(s: str) -> int:
  n = 0
  tail = len(s) - 1
  while (tail >= 0 and s[tail] == " "): tail -= 1
  while (tail >= 0 and s[tail] != " "):
    n += 1
    tail -= 1
  return n


if __name__ == "__main__":
  print(length_of_last_word("Hello world"))
  print(length_of_last_word_opt("skaff"))