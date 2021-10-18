# 7:09
from collections import defaultdict

class Solution:
    """
    https://leetcode.com/problems/exclusive-time-of-functions/
    validate the boundary

    """
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0 for i in range(n)]
        p_time = 0
        for i, log in enumerate(logs):
            id, action, time = log.split(':')
            id, time = int(id), int(time)
            if not stack:
                stack.append(id)
                continue
            # start
            if action == 'start':
                res[stack[-1]] += time - p_time
                stack.append(id)
                p_time = time
            # end
            else:
                p_id = stack.pop()
                res[p_id] += time - p_time + 1
                p_time = time + 1
        return res
