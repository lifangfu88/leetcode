# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional, List


class Solution:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
    bottom-up level order traversal of its nodes' values.

    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = deque([root])
        res = []
        while len(stack) > 0:
            level = []
            for i in range(len(stack)):
                node = stack.popleft()
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level)
        return res[::-1]
