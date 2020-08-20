def defang_ip_addr(address: str) -> str:
    """
    # 1108: Given a valid (IPv4) IP address, return a defanged version of that IP address.

    A defanged IP address replaces every period "." with "[.]".
    """
    ans = []
    for ch in address:
        if ch == ".":
            ans.append("[.]")
        else:
            ans.append(ch)

    return "".join(ans)


if __name__ == "__main__":
    address = "1.1.1.1"
    assert defang_ip_addr(address) == "1[.]1[.]1[.]1"

    print("Passed all tests!")
