import heapq


class Solution:
    """
    greedy + heapq

    """
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        greedy, heapq
        """

        if not events:
            return 0

        # sort by start then end
        events.sort(key = lambda c: (c[0], c[1]))
        res = 0
        # current date
        date = 1
        # index
        i, n = 0, len(events)
        options = []
        heapq.heapify(options)
        while i < n or options:
            # push all possible events
            while i < n and events[i][0] == date:
                heapq.heappush(options, events[i][1])
                i += 1
            # get rid of expired ones for current date
            while options and options[0] < date:
                heapq.heappop(options)
            # heapq top is what to be used (aka ending first)
            if options:
                ending = heapq.heappop(options)
                res += 1
            date += 1

        return res
