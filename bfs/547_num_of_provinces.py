from collections import defaultdict, deque


class Solution:
    """
    https://leetcode.com/problems/number-of-provinces/
    1. build graph
    2. if standalone, keep it
    3. if connected, BFS
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        if not len(isConnected) == len(isConnected[0]):
            return 0
        # neighbors
        nbrs = defaultdict(list)
        # provinces -> nodes
        ps = defaultdict(list)
        visited = set()

        for i, val in enumerate(isConnected):
            for j, n in enumerate(val):
                if n == 1:
                    nbrs[i].append(j)

        for c in nbrs.keys():
            if c in visited:
                continue
            # standalone city
            if len(nbrs[c]) == 1:
                ps[c] = c
                continue
            # connected city, BFS
            que = deque([c])
            while que:
                for _ in range(len(que)):
                    node = que.popleft()
                    if node in visited:
                        continue
                    ps[c].append(node)
                    que += nbrs[node]
                    visited.add(node)
        return len(ps)
