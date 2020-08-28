from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    """
    # 735: We are given an array asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, and the sign represents its direction 
    (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will 
    explode. If both are the same size, both will explode.

    Two asteroids moving in the same direction will never meet.
    """
    N = len(asteroids)

    stk = []
    remaining = [True for _ in range(N)]

    i = 0
    while i < N:
        ast = asteroids[i]

        if ast > 0:
            stk.append((ast, i))
            i += 1
        else:
            if not stk:
                i += 1
                continue

            prev_ast, prev_i = stk.pop()
            if abs(ast) == prev_ast:
                remaining[i] = False
                remaining[prev_i] = False
                i += 1
            elif abs(ast) > prev_ast:
                remaining[prev_i] = False
            else:
                remaining[prev_i] = False
                asteroids[i] = asteroids[prev_i]

    return [asteroids[i] for i, truth in enumerate(remaining) if truth]


if __name__ == "__main__":
    asteroids = [5, 10, -5]
    assert asteroid_collision(asteroids) == [5, 10]

    asteroids = [8, -8]
    assert asteroid_collision(asteroids) == []

    asteroids = [10, 2, -5]
    assert asteroid_collision(asteroids) == [10]

    asteroids = [-2, -1, 1, 2]
    assert asteroid_collision(asteroids) == asteroids

    print("Passed all tests!")
