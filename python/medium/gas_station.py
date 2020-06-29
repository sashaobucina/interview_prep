from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    # 134: There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to
    its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit once in the clockwise 
    direction, otherwise return -1.

    NOTE:
    - If there exists a solution, it is guaranteed to be unique.
    - Both input arrays are non-empty and have the same length.
    - Each element in the input arrays is a non-negative integer.
    """
    gas_remaining = total = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]

        if gas_remaining >= 0:
            gas_remaining += diff
        else:
            gas_remaining = diff
            start = i

        total += diff

    return start if total >= 0 else -1


if __name__ == "__main__":
    gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    assert can_complete_circuit(gas, cost) == 3

    gas, cost = [2, 3, 4], [3, 4, 3]
    assert can_complete_circuit(gas, cost) == -1

    print("Passed all tests!")
