def judge_circle(moves: str) -> bool:
    """
    # 657: There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of
    # its moves, judge if this robot ends up at (0, 0) after it completes its moves.

    The move sequence is represented by a string, and the character moves[i] represents its ith move.
    Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after
    it finishes all of its moves, return true. Otherwise, return false.

    NOTE: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the
    right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's
    movement is the same for each move.
    """
    dirs = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    x, y = 0, 0
    for move in moves:
        dx, dy = dirs[move]
        x += dx
        y += dy

    return x == 0 and y == 0


if __name__ == "__main__":
    assert judge_circle("UD")
    assert not judge_circle("LL")

    print("Passed all tests!")
