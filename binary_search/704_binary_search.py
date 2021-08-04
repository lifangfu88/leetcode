from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        basic binary search, avoid dead loop, pay attention to exit result

        :param nums:
        :param target:
        :return:
        """

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            midst = (end + start) // 2
            if nums[midst] < target:
                start = midst
            elif nums[midst] > target:
                end = midst
            else:
                return midst
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
