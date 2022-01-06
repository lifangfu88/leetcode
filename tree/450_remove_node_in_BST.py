class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # find target node to remove
        # if to remove root
        if root.val == key:
            return self.newRoot(root)
        # root is to keep, need to find the parent of target
        node = root
        while node:
            if node.left and node.left.val == key:
                node.left = self.newRoot(node.left)
                return root
            if node.right and node.right.val == key:
                node.right = self.newRoot(node.right)
                return root

            if node.val > key:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

    def newRoot(self, root):
        if not root.left and not root.right:
            return None
        if root.left and root.right:
            new_root = root.left
            node = new_root
            while node.right:
                node = node.right
            node.right = root.right
            root.left = None
            root.right = None
            return new_root
        if root.left:
            new_root = root.left
            root.left = None
            return new_root
        if root.right:
            new_root = root.right
            root.right = None
            return new_root