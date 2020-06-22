import math


def permutation_sequence(n: int, k: int) -> str:
    """
    # 60: The set [1,2,3,...,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.
    """
    fact = math.factorial(n)
    ints = list(range(1, n + 1))

    # base case
    if k == 1:
        return "".join(map(str, ints))

    if k == fact:
        return "".join(map(str, ints[::-1]))

    res = []
    remaining = len(ints)
    while remaining > 1:
        fact //= remaining
        idx = k // fact - 1 if k % fact == 0 else k // fact
        res.append(str(ints[idx]))
        ints.pop(idx)

        k = k % fact
        remaining -= 1

    return "".join(res + [str(ints[0])])


if __name__ == "__main__":
    assert permutation_sequence(n=3, k=3) == "213"

    assert permutation_sequence(n=4, k=9) == "2314"

    assert permutation_sequence(n=5, k=37) == "24135"

    print("Passed all tests!")