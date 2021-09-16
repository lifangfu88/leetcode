

class UnionFind:
    def __init__(self, n=0):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(x)
        return self.parent[x]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if not parent_a == parent_b:
            self.parent[parent_a] = parent_b





