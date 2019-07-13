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

def inorderTraversal(root: TreeNode) -> None:
  l = []
  def helper(root: TreeNode) -> None:
    if root.left:
      helper(root.left)
    l.append(root.val)
    if root.right:
      helper(root.right)
  print(l)

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
  print(isSameTree(t1, t2))
  print(maxDepth(t1))
  print(minDepth(t1))
  print(levelOrderTraversal(t1))
  print(reverseLevelOrderTraversal(t1))
  print(zigzagTraversal(t1))
  print(averageOfLevels(t1))