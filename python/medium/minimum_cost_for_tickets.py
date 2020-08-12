from typing import List


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    """
    # 983: In a country popular for train travel, you have planned some train travelling one year in advance.

    The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

    Train tickets are sold in 3 different ways:
        - a 1-day pass is sold for costs[0] dollars;
        - a 7-day pass is sold for costs[1] dollars;
        - a 30-day pass is sold for costs[2] dollars.

    The passes allow that many days of consecutive travel.
    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.
    """
    N = days[-1]
    dp = [0 for _ in range(N + 1)]

    next_i = 0
    for i in range(1, N + 1):
        if i != days[next_i]:
            dp[i] = dp[i - 1]
        else:
            one_day = dp[i - 1] + costs[0]
            seven_day = dp[i - 7] + costs[1] if i >= 7 else costs[1]
            thirty_day = dp[i - 30] + costs[2] if i >= 30 else costs[2]

            dp[i] = min(one_day, seven_day, thirty_day)
            next_i += 1

    return dp[N]


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    assert min_cost_tickets(days, costs) == 11

    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    assert min_cost_tickets(days, costs) == 17

    print("Passed all tests!")
