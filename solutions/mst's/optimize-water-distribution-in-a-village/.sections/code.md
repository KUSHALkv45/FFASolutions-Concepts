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
        
    
    
        
    
        
        