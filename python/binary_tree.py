class TreeNode:
  def __init__(self, x: int):
    self.val = x
    self.left = None
    self.right = None

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

if __name__ == "__main__":
  t1 = TreeNode(1)
  t2 = TreeNode(1)
  print(isSameTree(t1, t2))
  print(maxDepth(t1))
  print(minDepth(t1))