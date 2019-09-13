from collections import defaultdict

class DSU:
  def __init__(self):
    self.p = list(range(10001))

  def find(self, x):
    if self.p[x] != x:
      self.p[x] = self.find(self.p[x])
    return self.p[x]

  def union(self, x, y):
    self.p[self.find(x)] = self.find(y)

"""
Given a list accounts, each element accounts[i] is a list of strings, where the 
first element accounts[i][0] is a name, and the rest of the elements are emails 
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the 
same person if there is some email that is common to both accounts. Note that even 
if two accounts have the same name, they may belong to different people as people 
could have the same name. A person can have any number of accounts initially, but 
all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first 
element of each account is the name, and the rest of the elements are emails in 
sorted order. The accounts themselves can be returned in any order.
"""
def merge_accounts(accounts: list) -> list:
  dsu = DSU()
  em_to_name, em_to_id = {}, {}
  id = 0

  for acc in accounts:
    name = acc[0]
    for email in acc[1:]:
      em_to_name[email] = name
      if email not in em_to_id:
        em_to_id[email] = id
        id += 1
      dsu.union(em_to_id[acc[1]], em_to_id[email])

  ans = defaultdict(list)
  for email in em_to_name:
    ans[dsu.find(em_to_id[email])].append(email)

  return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

if __name__ == "__main__":
  accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
              ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

  merged_accounts = merge_accounts(accounts)

  expected = [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], 
              ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

  assert(merged_accounts == expected)
  print(merged_accounts)
