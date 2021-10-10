class Solution:
    """
    existing intervals that can be merged must be adjacent

    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]

        merged = newInterval
        pos = -1
        for i, intv in enumerate(intervals):
            if intv[0] > merged[1] or intv[1] < merged[0]:
                res.append(intv)
            else:
                if pos == -1:
                    pos = i
                merged[0] = min(intv[0], merged[0])
                merged[1] = max(intv[1], merged[1])
        res.insert(i, merged)
        return sorted(res)
