from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def get_importance(employees: List[Employee], _id: int) -> int:
    """
    # 690: You are given a data structure of employee information, which includes the employee's unique id, 
    their importance value and their direct subordinates' id.

    For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
    They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like 
    [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although 
    employee 3 is also a subordinate of employee 1, the relationship is not direct.

    Now given the employee information of a company, and an employee id, you need to return the total 
    importance value of this employee and all their subordinates.
    """
    def dfs(e: Employee) -> int:
        return e.importance + sum([dfs(e_map[s_id]) for s_id in e.subordinates])

    e_map = {e.id: e for e in employees}
    return dfs(e_map[_id])


if __name__ == "__main__":
    e3 = Employee(3, 3, [])
    e2 = Employee(2, 3, [])
    e1 = Employee(1, 5, [2, 3])

    employees = [e1, e2, e3]
    assert get_importance(employees, 1) == 11

    print("Passed all tests!")
