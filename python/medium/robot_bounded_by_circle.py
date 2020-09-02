def is_robot_bounded(instructions: str) -> bool:
    """
    # 1041: On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
        - "G": go straight 1 unit;
        - "L": turn 90 degrees to the left;
        - "R": turn 90 degress to the right.

    The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

    NOTE: Robot is bouded if robot is in original position, or direction facing is not north! (one-pass)
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_direction(balance):
        return balance % 4 if balance >= 0 else (balance + 4) % 4

    def execute(pos=(0, 0), balance=0):
        x, y = pos
        for instr in instructions:
            dr = get_direction(balance)

            if instr == "G":
                dx, dy = directions[dr]
                x += dx
                y += dy
            elif instr == "R":
                balance += 1
            else:
                balance -= 1

        return (x, y), balance

    pos, balance = execute()

    num_loops = 0
    if balance % 4 == 2:
        num_loops = 1
    elif (balance % 4 == 1) or (balance % 4 == 3):
        num_loops = 3

    if num_loops:
        for _ in range(num_loops):
            pos, balance = execute(pos, balance)

    return (pos == (0, 0)) and (balance % 4 == 0)


if __name__ == "__main__":
    instructions = "GGLLGG"
    assert is_robot_bounded(instructions)

    instructions = "GG"
    assert not is_robot_bounded(instructions)

    instructions = "GL"
    assert is_robot_bounded(instructions)

    print("Passed all tests!")
