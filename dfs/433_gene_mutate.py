import sys


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        self.min_leng = sys.maxsize
        bank_set = set(bank)
        #DFS
        cand = ['A', 'C', 'G', 'T']
        if not start or not end or not end in bank:
            return -1

        self.dfs(cand, start, end, set(), [], bank_set)
        if  self.min_leng == sys.maxsize:
            return -1

        return self.min_leng

    def dfs(self, cand, start, end, visited, path, bank):
        visited.add(start)
        for pos in range(len(start)):
            for c in cand:
                mutat = [x for x in start]
                mutat[pos] = c
                s_mu = ''.join(mutat)
                if s_mu == end:
                    self.min_leng = min(self.min_leng, len(path) + 1)
                if s_mu not in visited and s_mu in bank:
                    self.dfs(cand, s_mu, end, visited, path + [s_mu], bank)
