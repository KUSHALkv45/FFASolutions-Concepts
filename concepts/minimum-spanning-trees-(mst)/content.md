# Minimum Spanning Trees (Mst)

# Minimum Spanning Trees (MST)

```
PRIM's , Krushkal's are Algos  which can help us in finding the MST from a graph
MST features :  
- It should be a valid tree and connecting all nodes by atleast one path
- If There are N vertices then N-1 edges are required with no cycles ofcourse

- So Greedy Algo's are used here (it can't be optimized by dp in choosing subsets )
- PRIM's  :
- Start at a vertex and explore it's edges and add the shortest edge to the MST 
- use heap 
- Optimized space complexity will be 
- start at vertex and find the min distant vertex from our current vertex  and mark the shortest node as visited and add the edges from this vertex by updating distances 
- use a vis array and minDistances array  Time Complexity explore all the edges

- KRUSHKAL's is :
- sort the edges in increasing order and then add edges in increasing order only if they dont make a cycle in the current structure created so far
- union find is used

- here space complexity for normal algo's is O(Edges) and so we can use a optimized prim's approach for better space complexity




```
[graph.png]

``` python
class Solution:
    def minCostConnectPointsPRIMSOptmized(self, points: List[List[int]]) -> int:
        N = len(points)
        minDis = [inf] * N
        vis = [0] * N
        ans = 0
        cnt = 0
        minDis[0] = 0
        for i in range(N):
            u = -1

            for j in range(N):
                if vis[j] == 0 and (u == -1 or minDis[u] > minDis[j]):
                    u = j

            vis[u] = 1
            ans += minDis[u]
            cnt += 1

            if(cnt == N):
                return ans

            for j in range(N):
                if vis[j] == 0:
                    minDis[j] = min(
                        minDis[j],
                        abs(points[u][1] - points[j][1])
                        + abs(points[u][0] - points[j][0]),
                    )

        return ans

    def minCostConnectPointsKRUSHKAL(self, points: List[List[int]]) -> int:
        N = len(points)

        par = [i for i in range(N)]
        size = [0] * N

        edg = []

        for i in range(N):
            for j in range(i + 1, N):
                edg.append(
                    [
                        i,
                        j,
                        abs(points[i][1] - points[j][1])
                        + abs(points[i][0] - points[j][0]),
                    ]
                )

        edg = sorted(edg, key=lambda x: x[2])

        def findP(ver: int) -> int:
            if par[ver] != ver:
                par[ver] = findP(par[ver])
            return par[ver]

        ans = 0
        cnt = 0

        for i in range(len(edg)):
            v1, v2, wt = edg[i][0], edg[i][1], edg[i][2]

            p1 = findP(v1)
            p2 = findP(v2)

            if p1 != p2:
                cnt += 1
                if size[p1] > size[p2]:
                    size[p1] += size[p2]
                    par[p2] = p1
                    ans += wt
                else:
                    size[p2] += size[p1]
                    par[p1] = p2
                    ans += wt
            if cnt == N - 1:
                return ans

        return ans

    def minCostConnectPointsPRIMSnormal(self, points: List[List[int]]) -> int:

        N = len(points)
        vis = [0] * N

        comp = 0
        ans = 0

        heap = []

        heapq.heappush(heap, (0, 0))

        while heap:

            wt, node = heapq.heappop(heap)
            if vis[node]:
                continue
            vis[node] = 1
            comp += 1
            ans += wt
            if comp == N:
                return ans

            for i in range(N):
                if vis[i] == 0:
                    ewt, enode = (
                        abs(points[node][0] - points[i][0])
                        + abs(points[node][1] - points[i][1]),
                        i,
                    )
                    heapq.heappush(heap, (ewt, enode))
        return ans

```

## 🔗 Related Problems

- https://leetcode.com/problems/min-cost-to-connect-all-points/
