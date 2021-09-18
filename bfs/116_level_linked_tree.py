# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    Binary tree level traverse and add link
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        stack = deque([root])

        while stack:
            # create a dummy node for linked list
            pre_node = Node(-1)
            # length of current level, level traverse
            for i in range(len(stack)):
                curr_node = stack.popleft()
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)

                pre_node.next = curr_node
                pre_node = curr_node

        return root
