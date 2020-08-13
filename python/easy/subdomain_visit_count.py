from typing import List
from collections import defaultdict


def subdomain_visits(cpdomains: List[str]) -> List[str]:
    """
    # 811: A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, 
    we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". 
    When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" 
    and "com" implicitly.

    Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), 
    ollowed by a space, followed by the address. An example of a count-paired domain might be 
    "9001 discuss.leetcode.com".

    We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, 
    (in the same format as the input, and in any order), that explicitly counts the number of visits 
    to each subdomain.
    """
    visits = defaultdict(int)

    for cpdom in cpdomains:
        num_visits, domain = cpdom.split()
        num_visits = int(num_visits)

        sub_domains = domain.split(".")
        for i in range(len(sub_domains)):
            visits[".".join(sub_domains[i:])] += num_visits

    return [f"{ct} {dom}" for dom, ct in visits.items()]


if __name__ == "__main__":
    cpdomains = ["9001 discuss.leetcode.com"]
    expected = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    assert sorted(subdomain_visits(cpdomains)) == sorted(expected)

    cpdomains = [
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org"
    ]
    expected = [
        "901 mail.com",
        "50 yahoo.com",
        "900 google.mail.com",
        "5 wiki.org",
        "5 org",
        "1 intel.mail.com",
        "951 com"
    ]
    assert sorted(subdomain_visits(cpdomains)) == sorted(expected)

    print("Passed all tests!")
