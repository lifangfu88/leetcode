# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.bst(root)

        return self.res

    # return min, max, size
    def bst(self, root):
        if not root:
            return None
        left = self.bst(root.left)
        right = self.bst(root.right)

        if left and right:
            if left[1] < root.val < right[0]:
                size = left[2] + right[2] + 1
                self.res = max(self.res, size)
                return left[0], right[1], size
            else:
                return None
        if left and not root.right:
            if left[1] < root.val:
                size = left[2] + 1
                self.res = max(self.res, size)
                return left[0], root.val, size
            else:
                return None
        if right and not root.left:
            if root.val < right[0]:
                size = right[2] + 1
                self.res = max(self.res, size)
                return root.val, right[1], size
            else:
                return None
        # not left, not right
        if not root.left and not root.right:
            self.res = max(self.res, 1)
            return root.val, root.val, 1