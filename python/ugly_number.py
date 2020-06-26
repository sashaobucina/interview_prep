def is_ugly_number(num: int) -> bool:
    """
    # 263: Write a program to check whether a given number is an ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
    """
    if num <= 0:
        return False

    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5

    return num == 1


def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:
    """
    # 1201: (Ugly Number III) Write a program to find the n-th ugly number.

    Ugly numbers are positive integers which are divisible by a or b or c.

    Constraints:
        - 1 <= n, a, b, c <= 10^9
        - 1 <= a * b * c <= 10^18
        - It's guaranteed that the result will be in range [1, 2 * 10^9]
    """
    def gcd(a: int, b: int) -> int:
        """ Greatest common divisor. """
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a: int, b: int) -> int:
        """ Lowest common multiple. """
        return (a * b) // gcd(a, b)

    def count(k: int) -> int:
        """ Determine the # of nums divisible by a, b, or c in [1, k]. """
        na = k // a
        nb = k // b
        nc = k // c
        nab = k // lcm(a, b)
        nac = k // lcm(a, c)
        nbc = k // lcm(b, c)
        nabc = k // lcm(lcm(a, b), c)
        return na + nb + nc - nab - nac - nbc + nabc

    lo, hi = 0, 2 * (10 ** 9)
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = count(mid)

        if cnt >= n:
            if cnt == n and (mid % a == 0) and (mid % b == 0) and (mid % c == 0):
                return mid
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    assert is_ugly_number(6)
    assert not is_ugly_number(7)

    assert nth_ugly_number(3, a=2, b=3, c=5) == 4
    assert nth_ugly_number(7, a=7, b=7, c=7) == 49

    print("Passed all tests!")
