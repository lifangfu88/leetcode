from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        classic BFS algorithm, inner loop can only use range(len(stack))
        as stack is changing inside the loop, for each level, the length is
        decided when the traverse of last level finishes, aka, len(stack)


        :param root:
        :return:
        """

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
        return res
