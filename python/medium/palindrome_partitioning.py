from typing import List


def partition(s: str) -> List[List[str]]:
    """
    # 131: 
    """
    ans = []

    def backtrack(lst, idx):
        if idx == len(s):
            ans.append(lst)
            return

        for i in range(idx, len(s)):
            tmp = s[idx:i + 1]
            if tmp == tmp[::-1]:
                backtrack(lst + [tmp], i + 1)

    backtrack([], 0)
    return ans


if __name__ == "__main__":
    s = "aab"
    assert partition(s) == [["a", "a", "b"], ["aa", "b"]]

    print("Passed all tests!")
