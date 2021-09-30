//problem link: https://leetcode.com/problems/number-of-islands/
//problem statement: matrix 1 is land. 0 is water. find # of islands. move vertically/horizontally. 

class Solution {
    
    public void dfs(char[][] grid, int m, int n, int i, int j, boolean[][] visited){
        visited[i][j]= true;
        if(i+1<m && grid[i+1][j]== '1' && !visited[i+1][j]){
            dfs(grid,m,n,i+1,j,visited);
        }
        if(j+1<n && grid[i][j+1]== '1' && !visited[i][j+1]){
            dfs(grid,m,n,i,j+1,visited);
        }
        if(i-1>=0 && grid[i-1][j]== '1'&& !visited[i-1][j]){
            dfs(grid,m,n,i-1,j,visited);
        }
        if(j-1>=0 && grid[i][j-1]== '1' && !visited[i][j-1]){
            dfs(grid,m,n,i,j-1,visited);
        }
        
    }
    
    public int numIslands(char[][] grid) {
        int m= grid.length;
        int n= grid[0].length;
        boolean[][] visited= new boolean[m][n];
        int count= 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]== '1' && !visited[i][j]){
                    count+= 1;
                    dfs(grid,m,n,i,j,visited);   
                }
            }
        }
        return count;
    }
}