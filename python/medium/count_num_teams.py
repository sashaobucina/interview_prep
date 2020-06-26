from typing import List


def num_teams(rating: List[int]) -> int:
    """
    # 1395: There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

    You have to form a team of 3 soldiers amongst them under the following rules:
        - Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
        - A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
        where (0 <= i < j < k < n).
        - Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
    """
    n = len(rating)
    larger = [0] * n
    smaller = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            if rating[i] > rating[j]:
                smaller[i] += 1
            else:
                larger[i] += 1

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if rating[i] < rating[j]:
                ans += larger[j]
            else:
                ans += smaller[j]

    return ans


if __name__ == "__main__":
    rating = [2, 5, 3, 4, 1]
    assert num_teams(rating) == 3

    rating = [2, 1, 3]
    assert num_teams(rating) == 0

    rating = [1, 2, 3, 4]
    assert num_teams(rating) == 4

    print("Passed all tests!")
