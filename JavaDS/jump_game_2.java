//problem link: https://leetcode.com/problems/jump-game-ii/submissions/
//problem statement: array. min jumps to reach last index with max jump of crrent array element. 

import java.util.*;
import java.lang.*;

class jump_game_2 {
    public int jump(int[] nums) {
        int n= nums.length;
        int[] dp= new int[n];
        for(int i=1; i<n; i++){
            dp[i]= n+1;
        }
        dp[0]= 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<Math.min(n, i+nums[i]+1); j++){
                dp[j]= Math.min(dp[j], 1+dp[i]);
            }
        }
        return dp[n-1];
    }
}