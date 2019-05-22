def can_win_nim(n: int) -> bool:
  return (n < 4) or (n >= 5 and n % 4 != 0)

if __name__ == "__main__":
  print(can_win_nim(3))