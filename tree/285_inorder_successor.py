# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # smallest val > p
        # simple solution: inorder traverse, O(n)
        # improve: O(lgN)
        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res