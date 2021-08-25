# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    1. BST inorder traverse is a sorted list
    2. node val is distinct
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST inorder traverse is a sorted list
        """
        res = []
        self.inorder(root, res)
        return res == sorted([x for x in set(res)])

    def inorder(self, root, res):
        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

        return
