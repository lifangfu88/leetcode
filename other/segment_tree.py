class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

from collections import deque, defaultdict

def build_tree(input):
    '''
    input: list of nums
    output: root node of min segment tree
    '''
    res = []
    i2n = {}
    que = deque([TreeNode(n) for n in input])
    while len(que) > 1:
        level_size = len(que)
        for i in range(len(que)):
            n = que[i]
            node = TreeNode(n.val)
            i2n[i] = node
            if i % 2:
                # odd index
                parent = TreeNode((min(n.val, que[i - 1].val)))
                left = i2n[i - 1]
                right = i2n[i]
                parent.left = left
                parent.right = right
                left.parent = parent
                right.parent = parent
                que.append(left)
                res.append(parent)
        # append last node if input's length is odd
        if level_size % 2:
            i = len(que) - 1
            child = TreeNode(que[i].val)
            parent = TreeNode(que[i].val)
            child.parent = parent
            parent.left = child
            que.append(parent)
        for i in range(level_size):
            que.popleft()
    return que.pop()

if __name__ == '__main__':

    # build segment Tree with TreeNode
    input = [2, 5, 1, 4, 9, 3]
    root = build_tree(input)
    print(root)




