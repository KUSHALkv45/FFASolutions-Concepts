# optimize-water-distribution-in-a-village

## 💡 Idea

Problem statement :
```
Given an integer N, where N denotes the number of villages numbered 1 to N, an array wells[] where wells[i] denotes the cost to build a water well in the i'th city, a 2D array pipes in form of [X Y C] which denotes that the cost to connect village X and Y with water pipes is C. Your task is to provide water to each and every village either by building a well in the village or connecting it to some other village having water. Find the minimum cost to do so.
```

- imp point is we want to connect to water supply and this can be done by using a well or connecting with other houses which have water supply.
- So if houses are points on a graph and pipes work as edges b/w them and consider wells as a water supply point which has edge with evry node 
- So Now problem becomes simple MST problem and we find using Krushkal's or prim's

## ⏱️ Time & Space Complexity

```
Krushkal's TC : if N- vertices and pipes are "edges" - given constraint <= N we add N more to it 
so they are total of 2*N in krushkal's we sort them so O(NlogN) 

and then traversing and using union find (constant time O(4alpha) ) - so total will be O(NlogN + N)

SC : O(2N)

```

## 💻 Code

```python
from typing import List

def waterdistribution(n:int , edg : List[List[int]] , water : List[int]) -> int:
    
    size = [1] * (n+1)
    par = [i for i in range(n+1)]
    
    ans = 0
    
    def parent(i:int) -> int:
        if par[i] != i:
            par[i] = parent(par[i])
        return par[i]
    
    def union(u:int , v :int , wt:int) -> int :
        val = 0
        p1,p2 = parent(u),parent(v)
        
        if p1 != p2:
            val += wt
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                par[p2] = p1
            else:
                size[p2] += size[p1]
                par[p1] = p2
        return val
    edges = []
    
    for e in edg:
        edges.append(e)
    
    for i in range(n):
        edges.append([0,i+1,water[i]])
    
    edges = sorted(edges,key = lambda x : x[2])
    
    for i in range(len(edges)):
        u,v,wt = edges[i][0],edges[i][1],edges[i][2]
        ans += union(u,v,wt)

    return ans
    
print(waterdistribution(4, [[1, 2, 1], [1, 3, 3], [2, 3, 3], [3, 4, 1]], [1, 2, 1, 2]))
```

