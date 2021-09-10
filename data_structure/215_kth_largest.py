from typing import List
import heapq


class Solution:
    """
    the Kth largest element, using heap (priorityQ)
    tips: python heapq is a mini-heap

    time: Nlog(N)
    space: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums or k > len(nums) or k < 0:
            return None

        num = [v * -1 for v in nums]
        heapq.heapify(num)

        res = None
        while k > 0:
            res = heapq.heappop(num)
            k -= 1

        return res * -1
