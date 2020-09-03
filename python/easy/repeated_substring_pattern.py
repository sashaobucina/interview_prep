import math


def repeated_substring_pattern(s: str) -> bool:
    """
    # 459: Given a non-empty string check if it can be constructed by taking a substring of it and 
    appending multiple copies of the substring together. You may assume the given string consists of 
    lowercase English letters only and its length will not exceed 10000.
    """
    N = len(s)

    for i in range(N // 2):
        substr = s[:i+1]
        div, mod = divmod(N, i+1)

        if (mod == 0) and (substr * div == s):
            return True

    return False


def repeated_substring_pattern_RP(s: str) -> bool:
    """
    This solution uses the Rabin-Karp algorithm wo/ spurious hit/hash collision verification.

    Time complexity: O(n*sqrt(n))
    Space complexity: O(sqrt(n))
    """
    n = len(s)
    if n < 2:
        return False
    if n == 2:
        return s[0] == s[1]

    for div in range(int(math.sqrt(n)), 0, -1):
        if n % div == 0:
            divisors = [div]
            if div != 1:
                divisors.append(n // div)
            for l in divisors:
                first_hash = curr_hash = hash(s[:l])
                start = l
                while start != n and curr_hash == first_hash:
                    curr_hash = hash(s[start: start + l])
                    start += l

                if start == n and curr_hash == first_hash:
                    return True

    return False


if __name__ == "__main__":
    assert repeated_substring_pattern("abab")
    assert not repeated_substring_pattern("aba")
    assert repeated_substring_pattern("abcabcabcabc")

    assert repeated_substring_pattern_RP("abab")
    assert not repeated_substring_pattern_RP("aba")
    assert repeated_substring_pattern_RP("abcabcabcabc")

    print("Passed all tests!")
