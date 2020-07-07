from typing import List


def prison_after_N_days(cells: List[int], N: int) -> List[int]:
    """
    # 957: There are 8 prison cells in a row, and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the following rules:
        - If a cell has two adjacent neighbors that are both occupied or both vacant, 
        then the cell becomes occupied.
        - Otherwise, it becomes vacant.

    NOTE: that because the prison is a row, the first and the last cells in the row can't have two 
    adjacent neighbors.

    We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell 
    is occupied, else cells[i] == 0.

    Given the initial state of the prison, return the state of the prison after N days 
    (and N such changes described above.)
    """
    cnt = 0
    seen = set()

    for i in range(N):
        nxt = _next_state(cells)
        nxt_str = str(nxt)
        if nxt_str in seen:
            cells = prison_after_N_days(cells, N % cnt)
            break

        seen.add(nxt_str)
        cnt += 1
        cells = nxt

    return cells


def _next_state(cells: List[int]) -> List[int]:
    return [0] + [int(cells[i-1] == cells[i+1]) for i in range(1, 7)] + [0]


if __name__ == "__main__":
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    assert prison_after_N_days(cells, 7) == [0, 0, 1, 1, 0, 0, 0, 0]

    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    assert prison_after_N_days(cells, 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0]

    print("Passed all tests!")
