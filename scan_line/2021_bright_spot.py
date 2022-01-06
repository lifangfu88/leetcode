from collections import defaultdict
import sys
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brs = defaultdict(int)

        for l in lights:
            brs[l[0] - l[1]] += 1
            brs[l[0] + l[1] + 1] -= 1

        maxb = -sys.maxsize
        idx = -1
        br = 0
        for i in sorted(brs.keys()):
            br += brs[i]
            if br > maxb:
                maxb = br
                idx = i

        return idx


