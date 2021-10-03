# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    traverse each node, compare it as root to subroot and see if it's same tree
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if self.isSameTree(node, subRoot):
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False

    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1:
            return False
        if not node2:
            return False

        if not node1.val == node2.val:
            return False

        if self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right):
            return True

        return False
