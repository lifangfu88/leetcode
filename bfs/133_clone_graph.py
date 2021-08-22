# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque


class Solution:
    """
    1. find all the nodes, create clones
    2. create a mapping between old nodes and their clone
    3. for the link in original graph, create the link in the clone graph,
    as mapping exists
    """

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodes = self.bfs(node)

        mapping = {}
        for n in nodes:
            mapping[n] = Node(n.val, [])

        for n in nodes:
            for nei in n.neighbors:
                mapping[n].neighbors.append(mapping[nei])

        return mapping[node]

    def bfs(self, node: 'Node'):
        """
        bfs the graph, return nodes set

        :param node:
        :return:
        """
        que = deque([node])
        visited = set()
        while que:
            n = que.popleft()
            visited.add(n)

            for nei in n.neighbors:
                if nei not in visited:
                    que.append(nei)
        return visited
