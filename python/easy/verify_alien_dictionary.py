from typing import List


def is_alien_sorted(words: List[str], order: str) -> bool:
    """
    # 953: In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
    The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true 
    if and only if the given words are sorted lexicographicaly in this alien language.
    """
    d = {ch: i for i, ch in enumerate(order)}

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        should_continue = False
        for j in range(min(len(word1), len(word2))):
            ch1, ch2 = word1[j], word2[j]
            if d[ch1] > d[ch2]:
                return False
            elif d[ch1] < d[ch2]:
                should_continue = True
                break

        if not should_continue and len(word1) > len(word2):
            return False

        return True


if __name__ == "__main__":
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert not is_alien_sorted(words, order)

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert not is_alien_sorted(words, order)

    print("Passed all tests!")
