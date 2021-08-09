from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        if len(nums) <= 1:
            return nums
        # need to make sure there is at least one element on each side.
        mid = (len(nums)) // 2
        # sort left
        left = self.sortArray(nums[:mid])

        # sort right
        right = self.sortArray(nums[mid:])

        # merge into a sorted array

        return self.merge(left, right)


    def merge(self, left, right):
        """
        merge 2 sorted array into 1

        :param left: sorted array
        :param right: sorted array
        :return:
        """
        if not left:
            return right
        if not right:
            return left

        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]

        return res
