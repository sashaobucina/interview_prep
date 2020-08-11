from typing import List


def expand(S: str) -> List[str]:
    """
    # 1087: A string S represents a list of words.

    Each letter in the word has 1 or more options.  If there is one option, the letter 
    is represented as is.  If there is more than one option, then curly braces delimit the options. 
    For example, "{a,b,c}" represents options ["a", "b", "c"].

    For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

    Return all words that can be formed in this manner, in lexicographical order.
    """
    res = []

    def dfs(word: str, i: int) -> None:
        if i == len(S):
            res.append(word)
            return

        if S[i] != "{":
            dfs(word + S[i], i + 1)
        else:
            letters = []
            while S[i] != "}":
                if S[i].isalpha():
                    letters.append(S[i])
                i += 1

            for letter in sorted(letters):
                dfs(word + letter, i + 1)

    dfs("", 0)
    return res


if __name__ == "__main__":
    assert expand("{a,b}c{d,e}f") == ["acdf", "acef", "bcdf", "bcef"]
    assert expand("abcd") == ["abcd"]

    print("Passed all tests!")
