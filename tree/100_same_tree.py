from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    recursively iterate the nodes, same tree means:
    same value for current node AND:
    same value for the left child AND:
    same value for the right child

    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.rec(p, q)

    def rec(self, p, q):
        if not p and not q:
            return True
        if not p and q or p and not q:
            return False

        return p.val == q.val and self.rec(p.left, q.left) and self.rec(p.right, q.right)
