# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys
from typing import Optional

class BSTIterator:
    """
    at initialization, build the structure for iteration:
    1. list of in-order node, this problem will be solved
    2. map from val to node, supports arbitrary starting val iteration

    using recursion solution to build a in-order tree node list

    """


    def __init__(self, root: Optional[TreeNode]):
        self.cursor = TreeNode(-sys.maxsize)
        self.cursor.left = root
        self.val_to_node = {-sys.maxsize:self.cursor}
        self.val = [-sys.maxsize]
        self.inorder(root, self.val, self.val_to_node)


    def next(self) -> int:
        i = self.val.index(self.cursor.val)
        if -1 < i < len(self.val):
            self.cursor = self.val_to_node[self.val[i + 1]]
            return self.cursor.val
        return None




    def hasNext(self) -> bool:
        return -1 < self.val.index(self.cursor.val) < len(self.val) - 1




    def inorder(self, root, val, val_to_node):
        if not root:
            return

        self.inorder(root.left, val, val_to_node)
        val.append(root.val)
        val_to_node[root.val] = root
        self.inorder(root.right, val, val_to_node)

        return
