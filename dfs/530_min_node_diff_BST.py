# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/minimum-absolute-difference-in-bst/
    O(n)
    in order traverse, then find min
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        self.traverse(root, nodes)

        res = max(nodes)
        for i in range(len(nodes) - 1):
            if nodes[i + 1] - nodes[i] < res:
                res = nodes[i + 1] - nodes[i]
        return res

    def traverse(self, root, nodes):
        if not root:
            return
        self.traverse(root.left, nodes)
        nodes.append(root.val)
        self.traverse(root.right, nodes)
