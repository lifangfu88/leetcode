# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        level traverse, then use the last value
        benefit: flexible for follow up and requirement change
        disadvantage: space complexity

        https://leetcode.com/problems/binary-tree-right-side-view/
        :param root:
        :return:
        """

        if not root:
            return []

        stack = deque([root])

        tree_levels = []

        while len(stack) > 0:
            level = []
            for _ in range(len(stack)):
                node = stack.popleft()
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            tree_levels.append(copy.deepcopy(level))

        return [i[-1] for i in tree_levels]


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS level traverse, only keep the last node of each level

        :param root:
        :return:
        """
        if not root:
            return []

        res = []
        stack = deque([root])

        while len(stack) > 0:
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(node.val)
        return res
