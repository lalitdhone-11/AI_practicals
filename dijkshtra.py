import heapq
graph = {
    'A': [('B',2), ('C',3)],
    'B': [('A',2), ('C',1), ('D',4)],
    'C': [('A',3), ('B',1), ('D',5)],
    'D': [('B',4), ('C',5)]
}
def dijkshtra(graph,s):
    dist={node:float('inf') for node in graph}
    dist[s]=0
    heap=[(0,s)]
    while heap:   
        curr_dist,node=heapq.heappop(heap)
        if curr_dist>dist[node]:
            continue
        for neighbour,weight in graph[node]:
            new_dist=curr_dist+weight
            if new_dist<dist[neighbour]:
                dist[neighbour]=new_dist
                heapq.heappush(heap,(new_dist,neighbour))
    return dist

result=dijkshtra(graph,'A')
print(result)