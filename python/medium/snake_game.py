from typing import List
from collections import deque


class SnakeGame:
    """
    # 353: Design a Snake game that is played on a device with screen size = width x height.

    The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

    You are given a list of food's positions in row-column order. When a snake eats the food, its length 
    and the game's score both increase by 1.

    Each food appears one by one on the screen. For example, the second food will not appear until the 
    first food was eaten by the snake.

    When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
    """

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = deque(food)

        self._dr_map = {"U": (0, -1), "D": (0, 1), "R": (1, 0), "L": (-1, 0)}
        self.body = deque([(0, 0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.body[-1]
        dx, dy = self._dr_map[direction]

        # change position on screen based of direction given
        new_x, new_y = x + dx, y + dy

        # check if hit boundary
        if (new_x < 0) or (new_y < 0) or (new_x >= self.width) or (new_y >= self.height):
            return -1

        # normal movement w/ no events
        if not self.food or [new_y, new_x] != self.food[0]:
            self.body.popleft()
            if (new_x, new_y) in self.body:
                return -1
            self.body.append((new_x, new_y))

        # currently on food
        else:
            if (new_x, new_y) in self.body:
                return -1
            self.food.popleft()
            self.body.append((new_x, new_y))

        return len(self.body) - 1


if __name__ == "__main__":
    game = SnakeGame(3, 2, [[1, 2], [0, 1]])
    assert game.move("R") == 0
    assert game.move("D") == 0
    assert game.move("R") == 1
    assert game.move("U") == 1
    assert game.move("L") == 2
    assert game.move("U") == -1

    print("Passed all tests!")
