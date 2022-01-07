# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if root and root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        left = right = False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)

        if left or right:
            return True

        return False

    def sameTree(self, rootA, rootB):
        if not rootA and not rootB:
            return True

        if not rootA or not rootB:
            return False

        left = self.sameTree(rootA.left, rootB.left)
        right = self.sameTree(rootA.right, rootB.right)

        if left and right and rootA.val == rootB.val:
            return True
        return False

