def detect_capital_use(word: str) -> bool:
    """
    # 520: Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

        - All letters in this word are capitals, like "USA".
        - All letters in this word are not capitals, like "leetcode".
        - Only the first letter in this word is capital, like "Google".

    Otherwise, we define that this word doesn't use capitals in a right way.
    """
    cnt = 0
    first = False

    for i, ch in enumerate(word):
        if ch.isupper():
            if i == 0:
                first = True
            cnt += 1

    return (cnt == 0) or (first and cnt == 1) or (cnt == len(word))


if __name__ == "__main__":
    assert detect_capital_use("USA")
    assert detect_capital_use("leetcode")
    assert detect_capital_use("Google")
    assert not detect_capital_use("FlaG")

    print("Passed all tests!")