def arrange_coins(n: int) -> int:
    """
    # 441: You have a total of n coins that you want to form in a staircase shape, where every k-th 
    row must have exactly k coins.

    Given n, find the total number of full staircase rows that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.
    """
    left, right = 0, n
    while left <= right:
        k = (left + right) // 2
        curr = k * (k + 1) // 2

        if curr == n:
            return k

        if n < curr:
            right = k - 1
        else:
            left = k + 1

    return right


if __name__ == "__main__":
    assert(arrange_coins(5)) == 2
    assert(arrange_coins(205)) == 19

    print("Passed all tests!")
