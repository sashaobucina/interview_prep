from typing import List


def min_cost_to_move_chips(position: List[int]) -> int:
    """
    # 1217: We have n chips, where the position of the ith chip is position[i].

    We need to move all the chips to the same position, In one step, we can change the position of the 
    ith chip from position[i] to:
        - position[i] + 2 or position[i] - 2 with cost = 0.
        - position[i] + 1 or position[i] - 1 with cost = 1.

    Return the minimum cost needed to move all the chips to the same position.
    """
    odd = sum([1 for x in position if x % 2 == 1])
    even = len(position) - odd

    return min(odd, even)


if __name__ == "__main__":
    position = [1, 2, 3]
    assert min_cost_to_move_chips(position) == 1

    position = [2, 2, 2, 3, 3]
    assert min_cost_to_move_chips(position) == 2

    position = [1, 10000]
    assert min_cost_to_move_chips(position) == 1

    print("Passed all tests!")
