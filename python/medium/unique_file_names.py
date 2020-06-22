from typing import List


def get_folder_names(names: List[str]) -> List[str]:
    """
    # 1487: Given an array of strings names of size n. You will create n folders in your file system such that, 
    at the ith minute, you will create a folder with the name names[i].

    Since two files cannot have the same name, if you enter a folder name which is previously used, 
    the system will have a suffix addition to its name in the form of (k), where, k is the smallest 
    positive integer such that the obtained name remains unique.

    Return an array of strings of length n where ans[i] is the actual name the system will assign to 
    the ith folder when you create it.

    Time complexity: O(n) -> beats 98% of cases
    Space complexity: O(n) -> beats 100% of cases
    """
    res = []
    seen = {}

    for name in names:
        if name not in seen:
            seen[name] = 1
            res.append(name)
        else:
            new_name = name
            while new_name in seen:
                k = seen[name]
                seen[name] += 1
                new_name = f"{name}({k})"

            res.append(new_name)
            seen[new_name] = 1

    return res


if __name__ == "__main__":
    names = ["pes", "fifa", "gta", "pes(2019)"]
    assert get_folder_names(names) == ["pes", "fifa", "gta", "pes(2019)"]

    names = ["gta", "gta(1)", "gta", "avalon"]
    assert get_folder_names(names) == ["gta", "gta(1)", "gta(2)", "avalon"]

    names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
    assert get_folder_names(names) == [
        "onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"]

    names = ["wano", "wano", "wano", "wano"]
    assert get_folder_names(names) == ["wano", "wano(1)", "wano(2)", "wano(3)"]

    names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
    assert get_folder_names(names) == [
        "kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)"]

    names = ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]
    assert get_folder_names(names) == [
        "kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)", "kaido(2)(1)"]

    print("Passed all tests!")
