class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.shiftup(A, i)
        return A

    def shiftup(self, A, i):
        """
        NlogN
        from leaf node to shift up
        :param A:
        :param i:
        :return:
        """
        while i != 0:
            parent_i = (i - 1) // 2
            if A[parent_i] > A[i]:
                # need to swap
                A[i], A[parent_i] = A[parent_i], A[i]
                i = parent_i
            else:
                # current node meets heap requirement
                break


    def heapify_1(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.shiftdown(A, i)

    def shiftdown(self, A, index):
        """
        Heapify 的具体实现方法。时间复杂度为 O(n)，
        使用的是 siftdown 之所以是 O(n) 是因为从第 N/2 个位置开始往下 siftdown，
        那么就有大约 N/4 个数在 siftdown 中最多交换 1 次，N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。
        所以:
        O(N/4∗1+N/8∗2+N/16∗3+...+1∗LogN)=O(N)

        :param A:
        :param index:
        :return:
        """

        n = len(A)
        while i < n:
            left = i * 2 + 1
            right = i * 2 + 2
            min_i = i
            if left < n and A[left] < A[min_i]:
                min_i = left
            if right < n and A[right] < A[min_i]:
                min_i = right

            if min_i == i:
                break

            A[i], A[min_i] = A[min_i], A[i]
            i = min_i

