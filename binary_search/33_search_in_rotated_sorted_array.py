from typing import List

"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Key to this problem is: do not need to find out the pivot point, 
just reduce the size / scale of the problem based on different situation, 
aka, which side of the pivot does the mid point fall into. 


"""

class Solution:
    """
    @param nums: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    "==============================================================="
    """
    naive solution:
    """
    def search_2(self, nums: List[int], target: int) -> int:
        # solution:  1. find the pivot point with binary search
        # 2. binary search both sides of the pivot point respectively
        
        if not nums:
            return -1
        if len(nums) is 1:
            return -1 if target not in nums else 0
        
        
        pivot_index = self.find_pivot(nums)
        # pivot is the smallest element
        res_left = self.binary_search(nums[:pivot_index], target)
        
        res_right = self.binary_search(nums[pivot_index:], target)
        
        
        if res_left is not -1:
            return res_left
        
        if res_right is not -1:
            return res_right + pivot_index
        
        return -1
    
    
    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] is target:
                return mid
        
        if nums[start] is target:
            return start
        if nums[end] is target:
            return end
        
        return -1
        
    
    def find_pivot(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        
        while start + 1 < end:
            
            mid = (start + end) // 2
            if nums[start] < nums[end]:
                return start
            
            
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[start]:
                start = mid
            
        if nums[start] < nums[end]:
            return start
        return end
