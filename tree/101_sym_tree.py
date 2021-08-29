# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.sub_sym(root.left, root.right)

    def sub_sym(self, left, right):

        # 叶子节点
        if not left and not right:
            return True

        # 单侧为None
        if not left or not right:
            return False

        # 两侧值不相等
        if left.val != right.val:
            return False

        # mirror 交叉比较
        outer_sym = self.sub_sym(left.left, right.right)
        inner_sym = self.sub_sym(left.right, right.left)

        return outer_sym and inner_sym
