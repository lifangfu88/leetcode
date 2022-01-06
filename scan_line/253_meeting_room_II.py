from collections import defaultdict
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        need = defaultdict(int)

        for s, e in intervals:
            need[s] += 1
            need[e - 0.5] -= 1

        res = 0
        cur = 0
        for k in sorted(need.keys()):
            cur += need[k]
            res = max(res, cur)

        return res