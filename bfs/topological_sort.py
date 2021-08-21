"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque


class Solution:
    """
    root of child graph meets: indegree is 0
    BFS, reduce the indegree of neighbor by 1
    keep adding root of child graph into res list

    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        res = []
        indegree = self.get_indegree(graph)
        stack = deque([x for x in graph if indegree[x] == 0])
        while stack:
            node = stack.popleft()
            res.append(node)
            for n in node.neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    stack.append(n)

        return res

    def get_indegree(self, graph):
        """
        calculate indegree of each node
        :param graph:
        :return:
        """
        res = {x:0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                res[neighbor] += 1
        return res
