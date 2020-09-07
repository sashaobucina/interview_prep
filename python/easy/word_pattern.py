def word_pattern(pattern: str, str: str) -> bool:
    """
    # 290: Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and 
    a non-empty word in str.
    """
    words = str.split()
    if len(pattern) != len(words):
        return False

    ch_to_word = {}
    word_to_ch = {}
    for ch, word in zip(pattern, words):
        pword = ch_to_word.get(ch, None)
        pch = word_to_ch.get(word, None)

        if not pch and not pword:
            ch_to_word[ch] = word
            word_to_ch[word] = ch
        elif pch != ch or pword != word:
            return False

    return True


def word_pattern_opt(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) == len(words):
        return len(set(zip(words, pattern))) == len(set(pattern)) == len(set(words))

    return False


if __name__ == "__main__":
    assert word_pattern("abaa", "dog cat dog dog")
    assert word_pattern_opt("abaa", "dog cat dog dog")

    assert not word_pattern("aaaa", "dog cat dog dog")
    assert not word_pattern_opt("aaaa", "dog cat dog dog")

    print("Passed all tests!")
