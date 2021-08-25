from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    3 keys in recursion:
    1. condition to return
    2. action at each step
    3. definition of the recursion(function header)
    """

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        self.recurse(root, res)

        return res

    def recurse(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.recurse(root.left, res)
        self.recurse(root.right, res)

        return
