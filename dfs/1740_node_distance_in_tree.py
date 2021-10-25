# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    1. find LCA
    2. nodes on same side(direct distance) or both side of LCA(sum of 2 distance from LCA)

    """
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if not root or p == q:
            return 0

        lca = self.lca(root, p, q)

        l = self.dis(lca, p, 0)
        r = self.dis(lca, q, 0)

        return l + r

    def dis(self, root, x, depth):
        if not root:
            return None

        if root.val == x:
            return depth

        left = self.dis(root.left, x, depth + 1)
        right = self.dis(root.right, x, depth + 1)

        if left:
            return left
        if right:
            return right

    def lca(self, root, a, b):
        if not root:
            return None

        left = self.lca(root.left, a, b)
        right = self.lca(root.right, a, b)

        if (left and right) or (root.val == a or root.val == b):
            return root

        if left:
            return left
        if right:
            return right
