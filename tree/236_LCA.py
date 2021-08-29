
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    recursively traverse the tree, if run into p or q, return it, if run into sub-tree LCA, return it

    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return
        # root is the LCA
        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # p and q on each side
        if l and r:
            return root
        # LCA on left
        if l:
            return l
        # LCA on right
        if r:
            return r

        # no LCA exist
        return None
