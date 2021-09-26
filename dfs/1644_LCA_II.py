# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        先遍历 加入visited；如果已经存在，然后再找LCA
        时间空间都是O(n)
        """
        visited = set()
        self.visit(root, visited)
        if p not in visited or q not in visited:
            return None

        return self.helper(root, p, q)

    def visit(self, root, visited):
        if not root:
            return
        visited.add(root)
        self.visit(root.left, visited)
        self.visit(root.right, visited)

    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or not p or not q:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right
