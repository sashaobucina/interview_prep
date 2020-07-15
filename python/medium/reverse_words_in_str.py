def reverse_words(s: str) -> str:
    """
    # 151: Given an input string, reverse the string word by word.

    NOTE:
        - A word is defined as a sequence of non-space characters.
        - Input string may contain leading or trailing spaces. However, your reversed string should not
            contain leading or trailing spaces.
        - You need to reduce multiple spaces between two words to a single space in the reversed string.
    """
    return " ".join(reversed(s.split()))


if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world!  ") == "world! hello"
    assert reverse_words("a good    example") == "example good a"

    print("Passed all tests!")