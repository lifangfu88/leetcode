# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
import sys


class Solution:
    """
    https://leetcode.com/problems/binary-tree-vertical-order-traversal/
    O(n)
    key: moving to left => col_index - 1
         moving to right => col_index + 1
    """
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col2val = defaultdict(list)

        min_col, max_col = self.bfs(root, 0, col2val)
        res = []

        # col is a continuous space, so, with min + max, we know the full range
        # to save the sorting
        for k in range(min_col, max_col + 1):
            res.append(col2val[k])

        return res

    def bfs(self, root, col, map):
        if not root:
            return
        min_col, max_col = sys.maxsize, -sys.maxsize
        que = deque([(root, 0)])
        while que:
            for _ in range(len(que)):
                node, col = que.popleft()
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                map[col].append(node.val)
                if node.left:
                    que.append((node.left, col - 1))
                if node.right:
                    que.append((node.right, col + 1))

        return min_col, max_col
