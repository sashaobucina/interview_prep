from typing import List
from collections import defaultdict


def longest_str_chain(words: List[str]) -> int:
    """
    # 1048: Given a list of words, each word consists of English lowercase letters.

    Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in 
    word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

    A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a 
    predecessor of word_2, word_2 is a predecessor of word_3, and so on.

    Return the longest possible length of a word chain with words chosen from the given list of words.

    NOTE:
        - 1 <= words.length <= 1000
        - 1 <= words[i].length <= 16
        - words[i] only consists of English lowercase letters.
    """
    max_word = 0
    len_d = defaultdict(list)
    for word in words:
        len_d[len(word)].append(word)
        max_word = max(max_word, len(word))

    def _predecessor(word1, word2):
        i1 = i2 = 0
        while i2 < len(word2) and i1 < len(word1):
            if word1[i1] == word2[i2]:
                i1 += 1
            i2 += 1

            if (i2 - i1) > 1:
                return False

        return True

    d = {word: 1 for word in words}
    max_chain = 1
    for i in range(1, max_word + 1):
        for word in len_d[i]:
            for p_word in len_d[i - 1]:
                if _predecessor(p_word, word):
                    d[word] = max(d[word], d[p_word] + 1)
                    max_chain = max(max_chain, d[word])

    return max_chain


if __name__ == "__main__":
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    assert longest_str_chain(words) == 4

    print("Passed all tests!")
