from typing import List


class Solution:
    """
    https://leetcode.com/problems/container-with-most-water/

    when moving, update the short height

    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        water = 0

        while left < right:
            contain = min(height[right], height[left]) * (right - left)

            water = max(water, contain)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return water
