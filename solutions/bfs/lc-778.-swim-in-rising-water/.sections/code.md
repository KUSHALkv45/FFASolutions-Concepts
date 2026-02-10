```java
    public int swimInWater(int[][] grid) {
        int n = grid.length;
         // just like dijsktra's states use this for adding only when needed
        int[][] dist = new int[n][n]; 
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = grid[0][0];

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.offer(new int[]{0, 0, grid[0][0]});

        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int r = cur[0], c = cur[1], val = cur[2];
            if (r == n - 1 && c == n - 1) return val;

            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nc >= 0 && nr < n && nc < n) {
                    int newVal = Math.max(val, grid[nr][nc]);
                    if (newVal < dist[nr][nc]) {
                        dist[nr][nc] = newVal;
                        pq.offer(new int[]{nr, nc, newVal});
                    }
                }
            }
        }
        return -1;
    }

```

