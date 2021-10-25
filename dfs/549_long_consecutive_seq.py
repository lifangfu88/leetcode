# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_seq = 1
        self.seq(root, [1, 1])
        return self.max_seq

    def seq(self, root, leng):
        if not root:
            return leng

        plus, minus = leng[0], leng[1]
        if root.left:
            l_plus, l_minus = self.seq(root.left, leng)
            if root.val == root.left.val + 1:
                plus = max(plus, l_plus + 1)
            elif root.val == root.left.val - 1:
                minus = max(minus, l_minus + 1)
        if root.right:
            r_plus, r_minus = self.seq(root.right, leng)
            if root.val == root.right.val + 1:
                plus = max(plus, r_plus + 1)
            elif root.val == root.right.val - 1:
                minus = max(minus, r_minus + 1)

        self.max_seq = max(self.max_seq, plus + minus - 1)

        return [plus, minus]
