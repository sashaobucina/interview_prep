from typing import List


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    """
    # 636: On a single threaded CPU, we execute some functions.  Each function has a unique id between 
    0 and N-1.

    We store logs in timestamp order that describe when a function is entered or exited.

    Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, 
    "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means 
    the function with id 1 ended at the end of timestamp 2.

    A function's exclusive time is the number of units of time spent in this function. 
    NOTE: This does not include any recursive calls to child functions.

    The CPU is single threaded which means that only one function is being executed at a given time unit.

    Return the exclusive time of each function, sorted by their function id.
    """
    def parse_log(log: str):
        s = log.split(":")
        return int(s[0]), s[1], int(s[2])

    res = [0 for i in range(n)]
    f_id, _, time = parse_log(logs[0])

    stk = [f_id]
    prev = time
    for i in range(1, len(logs)):
        f_id, state, time = parse_log(logs[i])

        if state == "start":
            if stk:
                res[stk[-1]] += time - prev

            stk.append(f_id)
            prev = time

        else:
            res[stk.pop()] += time - prev + 1
            prev = time + 1

    return res


if __name__ == "__main__":
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    assert exclusive_time(2, logs) == [3, 4]

    print("Passed all tests!")
