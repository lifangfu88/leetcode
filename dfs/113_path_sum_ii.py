from typing import Optional
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    don't append the path upfront, if there is no pop afterwards


    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(root, targetSum, path, res)

        return res

    def dfs(self, node, tar, path, res):

        if not node:
            return

        if not node.left and not node.right and node.val == tar:
            path.append(node.val)
            res.append(copy.deepcopy(path))
            return

        tar -= node.val
        # path.append(node.val) won't work because it always keeps the current node
        # without popping it out
        self.dfs(node.left, tar, path + [node.val], res)
        self.dfs(node.right, tar, path + [node.val], res)
