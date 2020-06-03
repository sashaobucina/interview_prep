from typing import List


def two_city_sched_cost(costs: List[List[int]]) -> int:
    """
    # 1029: There are 2N people a company is planning to interview. The cost of flying the i-th person 
    to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

    Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

    NOTE:
    - 1 <= costs.length <= 100
    - It is guaranteed that costs.length is even.
    - 1 <= costs[i][0], costs[i][1] <= 1000
    """
    cost = 0
    n = len(costs)
    A, B = 0, 0
    sorted_costs = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)

    for cost_a, cost_b in sorted_costs:
        if A == n // 2:
            cost += cost_b
            B += 1
        elif B == n // 2:
            cost += cost_a
            A += 1
        elif cost_a < cost_b:
            cost += cost_a
            A += 1
        else:
            cost += cost_b
            B += 1

    return cost



if __name__ == "__main__":
    costs = [[10,20],[30,200],[400,50],[30,20]]
    assert two_city_sched_cost(costs) == 110

    print("Passed all tests!")