from typing import List


def find_strobogrammatic(n: int) -> List[str]:
    """
    # 247: A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Find all strobogrammatic numbers that are of length = n.
    """
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]

    pairs = [("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]

    def helper(n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        elif n == 1:
            return [["0"], ["1"], ["8"]]
        else:
            ans = []
            for mid in helper(n - 2):
                for pair in [("0", "0")] + pairs:
                    ans.append([pair[0]] + mid + [pair[1]])

            return ans

    ans = []
    for mid in helper(n - 2):
        for pair in pairs:
            ans.append("".join([pair[0]] + mid + [pair[1]]))

    return ans


if __name__ == "__main__":
    assert find_strobogrammatic(0) == [""]
    assert find_strobogrammatic(1) == ["0", "1", "8"]
    assert find_strobogrammatic(2) == ["11", "88", "69", "96"]
    assert find_strobogrammatic(3) == [
        "101", "808", "609", "906", "111", "818", "619", "916", "181", "888", "689", "986"]

    print("Passed all tests!")
