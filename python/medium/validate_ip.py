import re


def validate_IP(IP: str) -> str:
    """
    # 468: Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

    IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal 
    numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

    Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

    IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 
    16 bits. The groups are separated by colons (":"). For example, the address 
    2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among 
    four hexadecimal digits and some low-case characters in the address to upper-case ones, so 
    2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

    However, we don't replace a consecutive group of zero value with a single empty group using two 
    consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an 
    invalid IPv6 address.

    Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 
    02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

    NOTE: You may assume there is no extra space or special characters in the input string.
    """
    if IP.count(":") == 7:
        return "IPv6" if _validate_IPv6(IP) else "Neither"
    elif IP.count(".") == 3:
        return "IPv4" if _validate_IPv4(IP) else "Neither"
    else:
        return "Neither"


def _validate_IPv4(IP: str) -> bool:
    groups = IP.split(".")

    if len(groups) != 4:
        return False

    for digit in groups:
        if (not digit.isdigit()) or (digit.startswith("0") and len(digit) > 1) or not (0 <= int(digit) <= 255):
            return False

    return True


def _validate_IPv6(IP: str) -> bool:
    groups = IP.split(":")

    if len(groups) != 8:
        return False

    for hx in groups:
        if len(hx) > 4 or hx.startswith("-"):
            return False

        try:
            int(hx, 16)
        except ValueError:
            return False

    return True


def validate_IP_regex(IP: str) -> str:
    """
    NOTE: This solution uses regex to validate IPs.
    """
    chunk_ipv4 = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    ipv4_pattern = re.compile(
        r"^(" + chunk_ipv4 + r"\.){3}" + chunk_ipv4 + r"$")

    chunk_ipv6 = r"([0-9a-fA-F]{1,4})"
    ipv6_pattern = re.compile(
        r"^(" + chunk_ipv6 + r"\:){7}" + chunk_ipv6 + r"$")

    if ipv4_pattern.match(IP):
        return "IPv4"
    return "IPv6" if ipv6_pattern.match(IP) else "Neither"


if __name__ == "__main__":
    # testing IPv4
    IP = "127.0.0.1"
    assert validate_IP(IP) == "IPv4"

    IP = "256.256.256.256"
    assert validate_IP(IP) == "Neither"

    IP = "255.255.255"
    assert validate_IP(IP) == "Neither"

    IP = "255.255.255.01"
    assert validate_IP(IP) == "Neither"

    # testing IPv6
    IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    assert validate_IP(IP) == "IPv6"

    IP = "02001:0db8:85a3:0:0:8A2E:0370:7334"
    assert validate_IP(IP) == "Neither"

    IP = "2001:0db8:85a3::0:8A2E:0370:7334"
    assert validate_IP(IP) == "Neither"

    IP = "2001:0db8:85G3:0:0:8A2E:0370:7334"
    assert validate_IP(IP) == "Neither"

    IP = "20EE:Fb8:85a3:0:0:8A2E:0370:7334"
    assert validate_IP_regex(IP) == "IPv6"

    # done testing
    print("Passed all tests!")
