import math


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a, b = 8, 4
    assert gcd(a, b) == math.gcd(a, b)

    print("Passed all tests")
