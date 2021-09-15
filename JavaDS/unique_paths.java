//problem link: https://leetcode.com/problems/unique-paths/submissions/
//problem statement: unique paths in matrix moving only right and down

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp= new int[m][n];
        if(m==1 || n==1){
            return 1;
        }
        for(int i=1; i<m; i++){
            dp[i][0]= 1;
        }
        for(int i=1; i<n; i++){
            dp[0][i]= 1;
        }
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                dp[i][j]= dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
}