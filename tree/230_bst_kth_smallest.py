from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    k is indexed from 1
    https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        res = []

        self.rec(root, res)

        if k - 1 > len(res) - 1:
            return -1

        return res[k - 1]

    def rec(self, root, res):
        if not root:
            return

        self.rec(root.left, res)
        res.append(root.val)
        self.rec(root.right, res)

        return
