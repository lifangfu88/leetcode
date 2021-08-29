from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    base version of path sum ii



    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        res = []
        path = ''
        self.dfs(root, path, res)

        return res

    def dfs(self, root, path, res):
        if not root:
            return

        if not root.left and not root.right:
            path += '->' + str(root.val)
            # remove the first '->'
            res.append(path[2:])

        # backtracking without current node value
        self.dfs(root.left, path + '->' + str(root.val), res)
        self.dfs(root.right, path + '->' + str(root.val), res)
