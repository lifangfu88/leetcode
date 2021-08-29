# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)

        # 当其中一个子树的高度为0时，当前高度决定于另一棵子树
        if min_left * min_right == 0:
            return min_left + min_right + 1

        return 1 + min(min_left, min_right)
