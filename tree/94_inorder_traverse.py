# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    in-order recursively traverse the tree

    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return res

        self.recurse(root, res)

        return res



    def recurse(self, node, res):
        if not node:
            return

        if node.left:
            self.recurse(node.left, res)
        res.append(node.val)
        if node.right:
            self.recurse(node.right, res)

        return
