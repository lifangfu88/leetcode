# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = deque([root])
        res = []
        depth = 0
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.popleft()
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            # if odd depth, reverse the list of this level.
            if depth % 2:
                level = level[::-1]
            res.append(level)
            depth += 1
        return res
