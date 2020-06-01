import re


def is_palindrome(num: int) -> bool:
    # Special cases
    if (num < 0) or (num % 10 == 0 and num != 0):
        return False

    reverted_num = 0
    while num > reverted_num:
        reverted_num = (reverted_num * 10) + (num % 10)
        num = num // 10

    return num == reverted_num or num == reverted_num // 10


def isPalindrome(s: str) -> bool:
    """
    # 125: Given a string, determine if it is a palindrome, considering only alphanumeric characters 
    and ignoring cases.
    """
    s = re.sub(r"\W", "", s).lower()
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    assert not is_palindrome(123)
    assert is_palindrome(424)

    assert isPalindrome("A man, a plan, a canal: Panama")
    assert not isPalindrome("race a car")

    print("Passed all tests!")
