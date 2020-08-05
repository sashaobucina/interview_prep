from typing import List


def num_unique_emails(emails: List[str]) -> int:
    """
    # 929: Every email consists of a local name and a domain name, separated by the @ sign.

    For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

    Besides lowercase letters, these emails may contain '.'s or '+'s.

    If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

    If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

    It is possible to use both of these rules at the same time.

    Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?
    """
    email_set = set()
    for email in emails:
        local, domain = email.split("@")

        # ignore anything after '+' sign
        if "+" in local:
            local = local[:local.index("+")]

        # remove all periods
        local = local.replace(".", "")

        email_set.add(local + "@" + domain)

    return len(email_set)


if __name__ == "__main__":
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]
    assert num_unique_emails(emails) == 2

    print("Passed all tests!")
