# Lc 2328. Number Of Increasing Paths In A Grid

## 💡 Idea

```
Just dfs and memo

dfs and memoize the path counts
```

## ⏱️ Time & Space Complexity

```
TC : O(N) 
SC : O(N)
N - no of edges = n*m*4

```

## 💻 Code

```python
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        paths = [ [0 for _ in range(M)] for _ in range(N) ]

        def find(i:int,j : int,prev : int) -> int:
            if i < 0 or i >= N or j < 0 or j >= M:
                return 0
            if grid[i][j] <= prev:
                return 0
            if paths[i][j] > 0:
                return paths[i][j]
            
            ans = 1

            ans += find(i+1,j,grid[i][j]) + find(i-1,j,grid[i][j]) + find(i,j+1,grid[i][j]) + find(i,j-1,grid[i][j])

            paths[i][j] = ans

            return ans

        fin = 0

        for i in range(N):
            for j in range(M):
                fin =  (fin + find(i,j,-1)) % 1_000_000_007

        return fin % 1_000_000_007
```

