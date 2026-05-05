visit=set()
g={ 
  'A':['B','C'],
  'B':['A','C','D','E'],
  'C':['A','B','D'],
  'D':['B','C'],
  'E':[]
  }
def dfs(g,s):
   visit.add(s)
   print(s,end=" ")
   for c in g[s]:
     if c not in visit:
        dfs(g,c)

dfs(g,'A')