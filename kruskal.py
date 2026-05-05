class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    ds = DisjointSet(n)

    mst = []
    cost = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            cost += w

    return cost, mst
n = 4

# Edge list: (u, v, weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

cost, mst = kruskal(n, edges)

print("Minimum Cost:", cost)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")