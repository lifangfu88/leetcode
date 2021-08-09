from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # find a pivot point, compare value on both sides, put smaller to left, bigger to right recursively

        def quick_sort(start, end):

            if start >= end:
                return
            # key 1: pivot value, not index
            pivot_value = nums[(start + end) // 2]

            i = start
            j = end

            while i <= j:
                # key 2: value is <, index is <=
                while nums[i] < pivot_value and i <= j:
                    i += 1
                while nums[j] > pivot_value and i <= j:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            # key 3: unsorted is an overlap area
            quick_sort(start, j)
            quick_sort(i, end)
        quick_sort(0, len(nums) - 1)

        return nums
