from collections import defaultdict


def longest_dup_substring(S: str) -> str:
    """
    # 1044: Given a string S, consider all duplicated substrings: (contiguous) substrings of S that 
    occur 2 or more times.  (The occurrences may overlap.)

    Return any duplicated substring that has the longest possible length. 
    (If S does not have a duplicated substring, the answer is "".)

    Solution uses Robin-Karp algorithm with rolling hash and binary search

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    N = len(S)
    prime = (2 ** 63) - 1

    # rolling hash
    def valid(L: int) -> int:
        rolling_hash = 0
        last_power = pow(26, L, prime)

        for i in range(L):
            rolling_hash = (rolling_hash * 26 + ord(S[i])) % prime

        seen = {rolling_hash}
        for i in range(L, N):
            rolling_hash = (rolling_hash * 26 +
                            ord(S[i]) - last_power * ord(S[i - L])) % prime
            if rolling_hash in seen:
                return i - L + 1
            else:
                seen.add(rolling_hash)

        return -1

    # binary search
    lo, hi = 0, N - 1
    res = 0

    while lo < hi:
        mid = (lo + hi + 1) // 2
        valid_idx = valid(mid)

        if valid_idx != -1:
            lo = mid
            res = valid_idx
        else:
            hi = mid - 1

    return S[res: res + lo]


def longest_dup_substring_TLE(S: str) -> str:
    """
    This solution produces a TLE!

    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    if len(set(S)) == len(S):
        return ""

    N = len(S)
    substrings = []
    for i in range(N):
        for j in range(i+1, N+1):
            substrings.append(S[i:j])

    d = defaultdict(int)
    longest_duplicate = ""

    for sub in substrings:
        if d[sub] >= 1:
            if len(sub) > len(longest_duplicate):
                longest_duplicate = sub
        d[sub] += 1

    return longest_duplicate


if __name__ == "__main__":
    S = "banana"
    assert longest_dup_substring(S) == "ana"
    assert longest_dup_substring_TLE(S) == "ana"

    S = "abcd"
    assert longest_dup_substring(S) == ""
    assert longest_dup_substring_TLE(S) == ""

    print("Passed all tests!")
