from random import randint


def rand7() -> int:
    return randint(1, 7)


def rand10() -> int:
    """
    # 470: Given a function rand7 which generates a uniform random integer in the range 1 to 7, write 
    a function rand10 which generates a uniform random integer in the range 1 to 10.

    Do NOT use system's Math.random().
    """
    idx = 41
    while idx > 40:
        row = rand7()
        col = rand7()
        idx = col + (row - 1) * 7

    return 1 + (idx - 1) % 10


if __name__ == "__main__":
    assert rand10() in list(range(1, 10))

    print("Passed all tests!")
