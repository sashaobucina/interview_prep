from collections import deque

class TreeNode:
  def __init__(self, x: int):
    self.val = x
    self.left = None
    self.right = None

def invertTree(root: TreeNode):
  if not root:
    return None
  q = [root]
  while len(q) > 0:
    curr = q.pop(0)
    curr.left, curr.right = curr.right, curr.left
    if curr.right:
      q.append(curr.right)
    if curr.left:
      q.append(curr.left)
  return root

def invertTreeRec(root: TreeNode):
  if not root:
    return None
  if root.right:
    invertTreeRec(root.right)
  if root.left:
    invertTreeRec(root.left)
  root.left, root.right = root.right, root.left
  return root

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
  # compare current nodes
  if not p and not q:
    return True
  if (p and not q) or (q and not p) or (p.val != q.val):
    return False

  return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

def maxDepth(root: TreeNode) -> int:
  if not root:
    return 0
  return 1 + max(maxDepth(root.right), maxDepth(root.left))

def minDepth(root: TreeNode) -> int:
  if not root:
    return 0

  if not root.right and not root.left:
    return 1

  # No right subtree, recur down left subtree
  if not root.right:
    return 1 + minDepth(root.left)

  # No left subtree, recur down right subtree
  if not root.left:
    return 1 + minDepth(root.right)

  return 1 + min(minDepth(root.right), minDepth(root.left))

def isBalanced(root: TreeNode) -> bool:
  return isBalancedHelper(root) > -1

def isBalancedHelper(root: TreeNode) -> int:
  if not root:
    return 0

  lh = isBalancedHelper(root.left)
  if lh == -1:
    return -1
  
  rh = isBalancedHelper(root.right)
  if rh == -1:
    return -1
  
  if abs(lh - rh) > 1:
    return -1

  return 1 + max(lh, rh)

def levelOrderTraversal(root: TreeNode) -> list:
  if not root:
    return []
  res = []
  Q = []
  Q.append(root)

  while len(Q) > 0:
    level_size = len(Q)
    curr_level = []
    for i in range(level_size):
      root = Q.pop(0)
      if root.left:
        Q.append(root.left)
      if root.right:
        Q.append(root.right)
      curr_level.append(root.val)
    res.append(curr_level)
  return res

def reverseLevelOrderTraversal(root: TreeNode) -> list:
  if not root:
    return []
  res = []
  Q = []
  Q.append(root)

  while len(Q) > 0:
    level_size = len(Q)
    curr_level = []
    for i in range(level_size):
      root = Q.pop(0)
      if root.left:
        Q.append(root.left)
      if root.right:
        Q.append(root.right)
      curr_level.append(root.val)
    res = [curr_level] + res
  return res

def zigzagTraversal(root: TreeNode) -> list:
  if not root:
    return []
  res = []
  currLevel = []
  nextLevel = []
  currLevel.append(root)
  ltr = True

  while len(currLevel) > 0:
    curr = currLevel.pop()
    res.append(curr.val)
    if ltr:
      if curr.left:
        nextLevel.append(curr.left)
      if curr.right:
        nextLevel.append(curr.right)
    else:
      if curr.right:
        nextLevel.append(curr.right)
      if curr.left:
        nextLevel.append(curr.left)

    if len(currLevel) == 0:
      ltr = not ltr
      currLevel, nextLevel = nextLevel, currLevel
  return res

def averageOfLevels(root: TreeNode) -> list:
  if not root:
    return []
  res = []
  Q = deque([])
  Q.append(root)

  while len(Q) > 0:
    level_size = len(Q)
    curr_total = 0
    for i in range(level_size):
      root = Q.popleft()
      if root.left:
        Q.append(root.left)
      if root.right:
        Q.append(root.right)
      curr_total += root.val
    res.append(curr_total / level_size)

  return res

"""
Find the sum of all left leaves in a given binary tree.
"""
def sumOfLeftLeaves(root: TreeNode) -> int:
  if not root:
    return 0

  right = sumOfLeftLeaves(root.right)
  left = sumOfLeftLeaves(root.left)
  
  if root.left and isLeaf(root.left):
    return root.left.val + right + left
  else:
    return right + left

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
def sortedArrayToBST(nums: list) -> TreeNode:
  if len(nums) == 0:
    return None

  mid = len(nums) // 2
  root = TreeNode(nums[mid])
  root.left = sortedArrayToBST(nums[:mid])
  root.right = sortedArrayToBST(nums[mid+1:])
  return root

"""
Two Sum problem using BST
"""
def findTarget(root: TreeNode, k: int) -> bool:
  if not root:
    return False

  s, q = set(), [root]
  while len(q) > 0:
    curr = q.pop()
    if k - curr.val in s:
      return True
    s.add(curr.val)
    if curr.left:
      q.append(curr.left)
    if curr.right:
      q.append(curr.right)
  return False

def inOrderTraversal(root: TreeNode) -> list:
  arr = []
  def _recHelper(root: TreeNode, arr: list) -> None:
    if root.left:
      _recHelper(root.left, arr)
    arr.append(root.val)
    if root.right:
      _recHelper(root.right, arr)

  if root:
    _recHelper(root, arr)
  return arr

def postOrderTraversal(root: TreeNode) -> list:
  arr = []
  def _recHelper(root: TreeNode, arr: list) -> None:
    if root.left:
      _recHelper(root.left, arr)
    if root.right:
      _recHelper(root.right, arr)
    arr.append(root.val)

  if root:
    _recHelper(root, arr)
  return arr

def preOrderTraversal(root: TreeNode) -> list:
  arr = []
  def _recHelper(root: TreeNode, arr: list) -> None:
    arr.append(root.val)
    if root.left:
      _recHelper(root.left, arr)
    if root.right:
      _recHelper(root.right, arr)

  if root:
    _recHelper(root, arr)
  return arr

def preOrderTraversalIter(root: TreeNode) -> list:
  if not root:
    return []

  res, stk = [], [root]

  while len(stk) > 0:
    curr = stk.pop(len(stk) - 1)
    res.append(curr.val)
    if curr.right:
      stk.append(curr.right)
    if curr.left:
      stk.append(curr.left)

  return res

def recoverBST(root: TreeNode) -> None:
  if not root:
    return

  def _inorderHelper(root: TreeNode, first, prev, second) -> None:
    if not root:
      return root

    _inorderHelper(root.left, first, prev, second)
    if not prev:
      prev = root
    else:
      if root.val < prev.val:
        if not first:
          first = prev
        second = root
      prev = root
    _inorderHelper(root.right, first, prev, second)

  first, prev, second = None, None, None
  _inorderHelper(root, first, prev, second)
  if first and second:
    first.val, second.val = second.val, first.val

def isLeaf(root: TreeNode) -> bool:
  return not root.left and not root.right

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such 
that adding up all the values along the path equals the given sum.
"""
def hasPathSum(root: TreeNode, sum: int) -> bool:
  def _recHelper(root: TreeNode, sum: int) -> bool:
    if isLeaf(root) and sum == 0:
      return True

    ans = False
    if root.left:
      ans = ans or _recHelper(root.left, sum - root.left.val)
    if root.right:
      ans = ans or _recHelper(root.right, sum - root.right.val)
    return ans

  if root:
    return _recHelper(root, sum - root.val)
  return False

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's 
sum equals the given sum.
"""
def pathSumII(root: TreeNode, sum: int) -> list:
  solutionSet = []

  def _recHelper(root: TreeNode, sum: int, path: list) -> None:
    if sum == 0 and isLeaf(root):
      solutionSet.append(path.copy())

    if root.left:
      path.append(root.left.val)
      _recHelper(root.left, sum - root.left.val, path)
      path.pop(len(path) - 1)

    if root.right:
      path.append(root.right.val)
      _recHelper(root.right, sum - root.right.val, path)
      path.pop(len(path) - 1)

  if root:
    _recHelper(root, sum - root.val, [root.val])
  return solutionSet

"""
Given a binary tree, imagine yourself standing on the right side of it, return 
the values of the nodes you can see ordered from top to bottom.
"""
def rightSideView(root: TreeNode) -> list:
  rightMostValueAtDepth = dict()

  stk = [(root, 0)]
  maxDepth = -1

  while stk:
    node, depth = stk.pop()
    if node:
      maxDepth = max(maxDepth, depth)
      rightMostValueAtDepth.setdefault(depth, node.val)

      stk.append((node.left, depth + 1))
      stk.append((node.right, depth + 1))

  return [rightMostValueAtDepth[depth] for depth in range(maxDepth + 1)]

"""
#366 Leetcode - Find leaves of binary tree.

Given a binary tree, traverse the entire tree and return all the leaves in one level, all the nodes 
one above the leaves in the next level, and so on such that the root is always in the last level of 
resulting output array.

Input: [1, 2, 3, 4, 5]
Output: [[3, 4, 5], [2], [1]]
"""
def findLeaves(root: TreeNode) -> list:
  res = []

  def helper(curr: TreeNode) -> int:
    if curr == None:
      return -1

    ind = max(helper(curr.left), helper(curr.right)) + 1
    if len(res) > ind:
      res[ind].append(curr.val)
    else:
      res.append([curr.val])

    return ind

  helper(root)
  return res


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
  def equals(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
      return True
    if not s or not t:
      return False
    return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)

  def traverse(s: TreeNode, t: TreeNode) -> bool:
    return t and (equals(s, t) or traverse(s, t.left) or traverse(s, t.right))

  return traverse(s, t)

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

NOTE: - All of the nodes' values will be unique.
NOTE: - p and q are different and both values will exist in the binary tree.
"""
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
  stk = [root]
  parent = {root: None}

  while p not in parent or q not in parent:
    curr = stk.pop()

    if curr.left:
      parent[curr.left] = curr
      stk.append(curr.left)
    if curr.right:
      parent[curr.right] = curr
      stk.append(curr.right)

  ancestors = set()
  print(ancestors)

  while p:
    ancestors.add(p)
    p = parent[p]

  while q not in ancestors:
    q = parent[q]
  return q


def distance_k(root: TreeNode, target: TreeNode, k: int) -> list:
  """
  We are given a binary tree (with root node root), a target node, and an integer value K.

  Return a list of the values of all nodes that have a distance K from the target node. 
  The answer can be returned in any order.
  """
  ans = []

  def dfs(node: TreeNode):
    if not node:
      return -1
    elif node is target:
      subtree_add(node, 0)
      return 1
    else:
      L, R = dfs(node.left), dfs(node.right)
      if L != -1:
        if L == k:
          ans.append(node.val)
        subtree_add(node.right, L + 1)
        return  L + 1
      elif R != -1:
        if R == k:
          ans.append(node.val)
        subtree_add(node.left, R + 1)
        return R + 1
      else:
        return -1

  def subtree_add(node: TreeNode, dist: int):
    if not node:
      return
    elif node is target:
      ans.append(node.val)
    else:
      subtree_add(node.left, dist + 1)
      subtree_add(node.right, dist + 1)

  dfs(root)
  return ans


"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original 
BST is changed to the original key plus sum of all keys greater than the original key in BST.
"""
def convertGreaterBST(root: TreeNode) -> TreeNode:
  def incrementBST(node: TreeNode, val: int) -> int:
    if not node:
      return val

    node.val += incrementBST(node.right, val)
    return incrementBST(node.left, node.val)

  incrementBST(root, 0)
  return root


if __name__ == "__main__":
  t1 = TreeNode(3)
  t2 = TreeNode(9)
  t3 = TreeNode(20)
  t4 = TreeNode(15)
  t5 = TreeNode(7)
  t1.left = t2
  t1.right = t3
  t2.right = t5
  t2.left = t4
  print("is same tree?", isSameTree(t1, t2))
  print("max depth:", maxDepth(t1))
  print("min depth:", minDepth(t1))
  print("inOrder:", inOrderTraversal(t1))
  print("levelOrder:", levelOrderTraversal(t1))
  print("reverseLevelOrder:", reverseLevelOrderTraversal(t1))
  print("preOrder (recursive):", preOrderTraversal(t1))
  print("preOrder (iterative):", preOrderTraversalIter(t1))
  print("postOrder (recursive)", postOrderTraversal(t1))
  print("zigzag:", zigzagTraversal(t1))
  print("All nodes distance K from target:", distance_k(t1, t5, 2))
  print("sum of left leaves:", sumOfLeftLeaves(t1))
  print("average of levels:", averageOfLevels(t1))
  print("has path sum?", hasPathSum(t1, 19))
  print("right side view:", rightSideView(t1))
  print("path sum (show path):", pathSumII(t1, 27))
  print("find leaves of binary tree", findLeaves(t1))
  print("Is subtree?", isSubtree(t3, t1))
  print("Lowest common ancestor:", lowestCommonAncestor(t1, t3, t5).val)