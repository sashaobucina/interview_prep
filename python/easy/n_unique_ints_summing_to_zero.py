from typing import List


def sum_zero(n: int) -> List[int]:
    """
    # 1304: Given an integer n, return any array containing n unique integers such that they add up to 0.
    """
    a = range(1, n)
    return list(a) + [-sum(a)]


if __name__ == "__main__":
    for i in range(1000):
        assert sum(sum_zero(i)) == 0

    print("Passed all tests!")