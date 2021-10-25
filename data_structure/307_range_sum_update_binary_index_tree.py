class Solution:
    """
    https://leetcode-cn.com/problems/range-sum-query-mutable
    /solution/guan-yu-ge-lei-qu-jian-he-wen-ti-ru-he-x-41hv/

    https://leetcode.com/submissions/detail/576606037/

    可用于：区间求和，区间最（大/小）值
    """
    def __init__(self, nums):
        self.tree = [0] * (len(nums) + 1)
        self.nums = nums
        for i in range(len(nums)):
            k = i + 1
            while k <= len(nums):
                self.tree[k] += nums[i]
                # move up to parent node
                k += self._lowbit(k)

    def _lowbit(self, x):
        """
        :returns index of parent node

        x = 5 = 0b00000101
        -x = -5 = 0b11111011
        x&-x = 0b00000001
        will be handy to look up parent node
        """
        return x & -x

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= len(self.nums):
            # update current node
            self.tree[i] += diff
            # update all the upstream node
            i += self._lowbit(i)

    def sumRange(self, i, j):
        res = 0
        j += 1
        # find pre_sum_j
        # self._query(origin_j)
        while j:
            res += self.tree[j]
            # from top to leaf
            j -= self._lowbit(j)
        # find presum_i-1
        # self._query(i - 1)
        while i:
            res -= self.tree[i]
            i -= self._lowbit(i)
        # identical to self._query(origin_j) - self._query(i - 1)
        return res

    def _query(self, i):
        res = 0
        i += 1
        while i:
            res += self.tree[i]
            i -= self._lowbit(i)
        return res
