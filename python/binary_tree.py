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
  print("rever seLevelOrder:", reverseLevelOrderTraversal(t1))
  print("preOrder (recursive):", preOrderTraversal(t1))
  print("preOrder (iterative):", preOrderTraversalIter(t1))
  print("postOrder (recursive)", postOrderTraversal(t1))
  print("zigzag:", zigzagTraversal(t1))
  print("average of levels:", averageOfLevels(t1))
  print("has path sum?", hasPathSum(t1, 19))
  print("path sum (show path):", pathSumII(t1, 27))