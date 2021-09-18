from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/merge-two-binary-trees/
    4 scenarios dfs
    O(N)
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        rootc = self.dfs(root1, root2)

        return rootc

    def dfs(self, root1, root2):
        if not root1 and not root2:
            return None

        if root1 and root2:
            rootc = TreeNode(root1.val + root2.val)
            rootc.left = self.dfs(root1.left, root2.left)
            rootc.right = self.dfs(root1.right, root2.right)

        if root1 and not root2:
            rootc = TreeNode(root1.val)
            rootc.left = self.dfs(root1.left, None)
            rootc.right = self.dfs(root1.right, None)

        if root2 and not root1:
            rootc = TreeNode(root2.val)
            rootc.left = self.dfs(root2.left, None)
            rootc.right = self.dfs(root2.right, None)

        return rootc
