"""
https://www.lintcode.com/problem/178/
 Graph Valid Tree
"""
from collections import deque

class Solution:
    """
    solution:
    1. tree edge count = node count - 1
    2. check if it's connected

    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n or not edges:
            return False
        if len(edges) != n - 1:
            return False

        nei = {}
        for i in range(n):
            nei[i] = []

        nodes = set()
        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)
            nodes.add(a)
            nodes.add(b)

        que = deque([0])
        visited = {}
        while que:
            n = que.popleft()
            visited[n] = True
            for node in nei[n]:
                if node not in visited:
                    que.append(node)

        print(len(visited), )
        return len(visited) == len(nodes)



if __name__ == '__main__':

    s = Solution()
    print(s.validTree(10,[[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]))
