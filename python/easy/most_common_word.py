import string
from typing import List
from collections import defaultdict


def most_common_word(paragraph: str, banned: List[str]) -> str:
    """
    # 819: Given a paragraph and a list of banned words, return the most frequent word that is not in 
    the list of banned words.

    It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

    Words in the list of banned words are given in lowercase, and free of punctuation.
    Words in the paragraph are not case sensitive.

    The answer is in lowercase
    """
    # remove all punctuation and make paragraph case insensitive
    exclude = set(string.punctuation)
    paragraph = "".join(
        ch.lower() if ch not in exclude else " " for ch in paragraph)

    # count all occurences of non-banned words
    banned = set(banned)
    d = defaultdict(int)
    for word in paragraph.split():
        if not word in banned:
            d[word] += 1

    # extract most frequent non-banned word
    _max, res = 0, ""
    for word, count in d.items():
        if count > _max:
            _max = count
            res = word

    return res


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    assert most_common_word(paragraph, ["hit"]) == "ball"

    print("Passed all tests!")
