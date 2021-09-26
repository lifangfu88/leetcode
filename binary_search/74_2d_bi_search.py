from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        2-D binary search, start from row
        """
        start, end = 0, len(matrix) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid

        if matrix[start][0] == target or matrix[end][0] == target:
            return True
        # ensures that matrix[start] >= target
        if matrix[end][0] < target:
            return self.one_d_search(matrix[end], target)
        return self.one_d_search(matrix[start], target)

    def one_d_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target or nums[end] == target:
            return True

        return False
