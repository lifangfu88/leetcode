
class Solution:
    """
    https://leetcode-cn.com/problems/range-sum-query-mutable
    /solution/xian-duan-shu-zu-shou-hui-tu-xiang-yi-qing-er-chu-/
    """

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * self.n * 2
        # update leaf
        for i in range(self.n, 2*self.n):
            self.tree[i] = nums[i - self.n]
        # from bottom to top
        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[2*i + 1]

    def update(self, pos, val):
        # index of leaf node
        pos += self.n
        # update leaf node
        self.tree[pos] = val
        # from bottom to top, update upstream branch
        while pos > 0:
            left_indx = right_indx = pos
            # pos is a left node, move right by 1 to update right_index
            if pos % 2 == 0:
                right_indx += 1
            else:
                left_indx -= 1
            self.tree[int(pos // 2)] = self.tree[left_indx] + self.tree[right_indx]
            pos = int(pos // 2)

    def sumRange(self, i, j):

        res = 0
        l = self.n + i
        r = self.n + j
        # 左奇右偶
        while r >= l:
            # left end is a right node, take it and move rightwards by 1 and // 2 to get parent node index of next node
            # else get parent node by // 2
            if l % 2 == 1:
                res += self.tree[l]
                l += 1

            # right end is a left node, take it and move leftwards by 1, // 2 to get parent node index of next node
            # else, get parent node by //2
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l = int(l // 2)
            r = int(r // 2)
        return res
