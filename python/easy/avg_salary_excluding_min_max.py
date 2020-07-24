from typing import List


def average(salary: List[int]) -> float:
    """
    # 1491: Given an array of unique integers salary where salary[i] is the salary of the employee i.

    Return the average salary of employees excluding the minimum and maximum salary.
    """
    _min = float("inf")
    _max = -float("inf")
    _sum = 0

    N = len(salary)
    for p in salary:
        _max = max(_max, p)
        _min = min(_min, p)

        _sum += p

    return (_sum - _min - _max) / (N - 2)


if __name__ == "__main__":
    salary = [4000, 3000, 1000, 2000]
    assert average(salary) == 2500.00000

    print("Passed all tests!")
