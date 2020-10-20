import nltk
from nltk.corpus import words


word_list = words.words()

def f(s, n):
    res = []
    for x in _permutations(s, n):
        _x = "".join(x)
        if _x in word_list:
            res.append(_x)

    return res


def _permutations(word, n):
    res = []

    visited = set()
    def backtrack(s):
        if len(s) == n:
            res.append(s)
            return

        for i in range(len(word)):
            if i not in visited:
                visited.add(i)
                backtrack(s + word[i])
                visited.remove(i)

    backtrack("")

    return set(res)

if __name__ == "__main__":
    letters = "ybwsau"
    print(f"3 words: {sorted(f(letters, 3))}")
    print(f"4 words: {sorted(f(letters, 4))}")
    print(f"5 words: {sorted(f(letters, 5))}")
    print(f"6 words: {sorted(f(letters, 6))}")