class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/second-minimum-node-in-a-binary-tree
    brute-force: traverse, then compare one by one

    better O(n): stop traverse when node.val > current second min node
    as there is a condition:
    child.val >= parent.val
    """
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        smallest = root.val

        second_s = self.dfs(root, smallest)
        if second_s:
            return second_s
        return -1

    def dfs(self, root, smallest):
        if not root.val == smallest:
            return root.val

        if root.left and root.right:
            l = self.dfs(root.left, smallest)
            r = self.dfs(root.right, smallest)
            if l and r:
                return min([l, r])
            if l:
                return l
            if r:
                return r

        if root.left:
            return self.dfs(root.left, smallest)

        if root.right:
            return self.dfs(root.right, smallest)
