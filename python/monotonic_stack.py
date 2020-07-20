from typing import List


def prev_less_element(A: List[int]) -> List[int]:
    """
    Find the previous less element for each element in O(n) time.

    Return list of indices signifying this.
    """
    in_stk = []
    prev_less = [-1] * len(A)

    for i in range(len(A)):
        while in_stk and A[in_stk[-1]] > A[i]:
            in_stk.pop()

        prev_less[i] = -1 if not in_stk else in_stk[-1]
        in_stk.append(i)

    return prev_less


def next_less_element(A: List[int]) -> List[int]:
    """
    Find the next less element for each element in O(n) time.

    Return list of indices signifying this.
    """
    in_stk = []
    next_less = [-1] * len(A)

    for i in range(len(A)):
        while in_stk and A[in_stk[-1]] > A[i]:
            x = in_stk.pop()
            next_less[x] = i

        in_stk.append(i)

    return next_less


if __name__ == "__main__":
    """
    Monotonic stack: stack in which elements always have an increasing pop order.
    """
    A = [3, 7, 8, 4]

    assert prev_less_element(A) == [-1, 0, 1, 0]
    assert next_less_element(A) == [-1, 3, 3, -1]

    print("Passed all tests!")
