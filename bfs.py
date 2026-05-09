from collections import deque
g={ 
  'A':['B','C'],
  'B':['A','C','D','E'],
  'C':['A','B','D'],
  'D':['B','C'],
  'E':[]
  }
vis=set(['A'])
q=deque(['A'])
def bfs(vis,q,g):
    if not q:
        return
     
    curr=q.popleft()
    print(curr,end=" ")
    for c in g[curr]:
        if c not in vis:
            vis.add(c)
            q.append(c)
    bfs(vis,q,g)

bfs(vis,q,g)
