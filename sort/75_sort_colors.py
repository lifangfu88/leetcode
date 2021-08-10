from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/sort-colors/
        Do not return anything, modify nums in-place instead.
        in-place: quick sort

        """
        def sort(start, end):

            if start >= end:
                return

            i, j = start, end
            pivot = nums[(start + end) // 2]

            while i <= j:
                while i <= j and nums[i] < pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            sort(i, end)
            sort(start, j)

        sort(0, len(nums) - 1)

    def sort_olors(self, nums: List[int]) -> None:
        """
        O(n), as there are only 3 values, smallest to front and largest to the end

        """
        start, end = 0, len(nums) - 1
        mid = start

        # condition to stop is mid > end
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 2:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1

            else:
                mid += 1
