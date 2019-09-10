def n_copies(s: str, n: int) -> str:
  if n < 1:
    return ""
  elif n == 1:
    return s
  else:
    return s + n_copies(s, n - 1)

if __name__ == "__main__":
  print(n_copies("Hello", 3))