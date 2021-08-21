from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        https://leetcode.com/problems/course-schedule/
        1. build graph
        2. get in_degree map
        3. topological sort
        4. compoare the result length vs course_num

        """
        if not numCourses or not prerequisites:
            return True
        res = []
        # assign course index from 0 to num - 1
        indegree = [0] * numCourses

        # use dict[int: [int]] to represent graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for node_1, node_2 in prerequisites:
            graph[node_2].append(node_1)
            indegree[node_1] += 1

        stack = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)

        # start to BFS
        while stack:
            node = stack.popleft()
            res.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    stack.append(n)
        return len(res) == numCourses
