from collections import defaultdict, deque
from typing import List


class Solution:
    """
    time: O(n)
        it is a loop, every node in the loop has the same path
        https://leetcode.com/problems/array-nesting/solution/
    """
    def arrayNesting(self, nums: List[int]) -> int:
        sk = defaultdict(set)
        for i, k in enumerate(nums):
            self.bfs(i, nums, sk)

        leng_max = -1
        for s in sk.values():
            leng_max = max(leng_max, len(s))

        return leng_max

    def bfs(self, index, nums, sk):
        if index in sk:
            return
        que = deque([index])
        visited = set()
        while que:
            for _ in range(len(que)):
                i = que.popleft()
                if i in visited:
                    # it is a loop, every node in the loop has the same path
                    for v in visited:
                        sk[v] = visited
                    return visited
                visited.add(i)
                que.append(nums[i])
        return
