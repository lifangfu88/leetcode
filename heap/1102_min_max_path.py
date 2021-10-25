import sys
import heapq

# BFS + max cost path
class Solution:
    """
    Dijkustri to find min_cost path
    here is to find the most expansive one(max heap) at each BFS step
    then, refresh the min overall value

    BFS + heap

    """
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        path =[(-grid[0][0], 0, 0)]

        heapq.heapify(path)
        max_min = sys.maxsize

        stop = [len(grid) - 1, len(grid[0]) - 1]
        visited = set((0, 0))

        while path:
            val, x, y = heapq.heappop(path)

            max_min = min(max_min, -val)
            if x == stop[0] and y == stop[1]:
                return max_min

            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if not -1 < nx < len(grid) or not -1 < ny < len(grid[0]):
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((x, y))
                heapq.heappush(path, (-grid[nx][ny], nx, ny))
        return -1
