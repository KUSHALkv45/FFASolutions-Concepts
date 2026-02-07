
    public int orangesRotting(int[][] grid) {
        Queue<int []> q = new LinkedList<>();
        int m = grid.length; int n = grid[0].length;
        int count = 0;
        for(int i = 0 ;i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(grid[i][j] != 0){
                    count++;
                    
                }
                if(grid[i][j] == 2){
                    count--;
                    q.add(new int[]{i,j});
                    grid[i][j] = 0;
                }
            }
        }

        int ans = 0;
        while(!q.isEmpty()){
            if(count == 0){
                return ans;
            }
            int s = q.size();
            while(s-- > 0){
                int [] p = q.poll();
                int i = p[0];
                int j = p[1];
                if(check(i-1,j,m,n,grid)){
                    q.add(new int[]{i-1,j});
                    count--;

                }
                if(check(i+1,j,m,n,grid)){
                    q.add(new int[]{i+1,j});
                    count--;

                }
                if(check(i,j-1,m,n,grid)){
                    q.add(new int[]{i,j-1});
                    count--;

                }
                if(check(i,j+1,m,n,grid)){
                    q.add(new int[]{i,j+1});
                    count--;

                }

            }
            ans++;
        }
        return count == 0 ? 0 : -1;
    }
    private boolean check(int i , int j , int m , int n ,  int[][] grid){
        if(i >= 0 && i < m && j >= 0 && j < n  && grid[i][j] == 1){grid[i][j] = 0 ;return true;}
        return false;
    }
