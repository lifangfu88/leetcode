from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    memorize visited nodes, add the branch sum into list,
    verify if the target is in list at the end

    can also change list to set()

    O(N)
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        sum_b = []

        self.dfs(0, sum_b, root)

        return targetSum in sum_b

    def dfs(self, su, sum_b, node):
        if not node:
            return

        su += node.val
        if not node.left and not node.right:
            sum_b.append(su)
        if node.left:
            self.dfs(su, sum_b, node.left)

        if node.right:
            self.dfs(su, sum_b, node.right)

        return
