from collections import defaultdict, deque
from typing import List


class Solution:
    """
    1. create the neighbor graph
    2. BFS each node, avoid duplicate visit
    3. each BFS path is one province

    time: O(n^2)
    space: O(n)

    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        if not len(isConnected) == len(isConnected[0]):
            return 0
        # neighbors, to form graph
        nbrs = defaultdict(list)
        # provinces
        ps = defaultdict(list)
        # avoid duplicated key
        visited = set()

        for i, val in enumerate(isConnected):
            for j, n in enumerate(val):
                if n == 1:
                    nbrs[i].append(j)

        for c in nbrs.keys():
            if c in visited:
                continue
            if len(nbrs[c]) == 1:
                ps[c] = c
                continue
            que = deque([c])
            while que:
                for _ in range(len(que)):
                    node = que.popleft()
                    if node in visited:
                        continue
                    # key point: ps key is on c
                    ps[c].append(node)
                    que += nbrs[node]
                    visited.add(node)
        return len(ps)
