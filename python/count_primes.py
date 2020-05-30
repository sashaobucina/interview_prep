def count_primes(n: int) -> int:
    """ # 204: Count the number of prime numbers less than a non-negative number, n. """
    count = 0
    not_prime = [False] * n
    for i in range(2, n):
        if not not_prime[i]:
            count += 1
            j = 2
            while i * j < n:
                not_prime[i * j] = True
                j += 1

    return count


if __name__ == "__main__":
    assert count_primes(10) == 4

    print("Passed all tests!")
