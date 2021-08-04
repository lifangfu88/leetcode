from typing import List

"""
in this case, how to continue bi-search when nums[mid] == target?
by splitting the problem into 2 part, look for the start and end separately

"""



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        return [self.binary_search_first(nums, target), self.binary_search_last(nums, target)]

    def binary_search_first(self, nums, target):
        """
        find first appearance

        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def binary_search_last(self, nums, target):
        """
        find last appearance

        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
