# 7:49
from typing import List

# both DFS and BFS can solve this

DIR = [[0, 1], [0, -1], [-1, 0], [1, 0]]


class Solution:
    """
    https://leetcode.com/problems/word-search/
    DFS
    time: O(3^len(word))
    """
    def exist(self, board: List[List[str]], word: str) -> bool:

        # avoid searching when impossible
        word_set = set([i for i in word])
        board_set = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                board_set.add(board[i][j])

        if not word_set.issubset(board_set):
            return False

        # start to search
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    res = self.dfs(board, i, j, word[0], word, set())
                    if res:
                        return True
        return False

    def dfs(self, board, i, j, path, target, visited):
        # cannot be used repeatedly
        if (i, j) in visited:
            return
        if path == target:
            return True
        if len(path) > len(target):
            return
        if path[-1] != target[len(path) - 1]:
            return

        for dx, dy in DIR:
            x = i + dx
            y = j + dy
            if not (-1 < x < len(board) and -1 < y < len(board[i])):
                continue
            visited.add((i, j))
            res = self.dfs(board, x, y, path + board[x][y], target, visited)
            visited.remove((i, j))
            if res:
                return True
