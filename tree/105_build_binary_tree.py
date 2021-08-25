# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
from pre order, find root; from in order, find left child-tree and right child-tree

recursively build the tree

"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        root = TreeNode(preorder[0])

        i = inorder.index(preorder[0])
        if len(inorder) < 2:
            return root


        left_in, right_in = inorder[:i], inorder[i + 1:]
        left_pre, right_pre = preorder[1: len(left_in) + 1], preorder[len(left_in) + 1 :]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root
