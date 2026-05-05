import heapq
g = {
    'A': [('B',2), ('C',3)],
    'B': [('A',2), ('C',1), ('D',4)],
    'C': [('A',3), ('B',1), ('D',5)],
    'D': [('B',4), ('C',5)]
}
def prims(g,s):
    visited=set()
    min_heap=[(0,s,None)]
    t_weight=0
    mst_edges=[]
    while min_heap:
        weight,node,parent=heapq.heappop(min_heap)
        if node in visited:
             continue
        visited.add(node)
        t_weight+=weight

        if parent is not None:
            mst_edges.append((parent,node,weight))
        for neighbour,egde_weight in g[node]:
              if neighbour not in visited:
                heapq.heappush(min_heap,(egde_weight,neighbour,node))
    return t_weight,mst_edges


cost,edges=prims(g,'A')
print(cost)
print("edges:")
print(edges)