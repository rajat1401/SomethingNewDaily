//problem link: https://leetcode.com/problems/house-robber/submissions/
//problem statement:given array with house values, can't rob any 2 adjacent houses. maximise rob sum.

//SEMI-OPTIMAL
import java.util.*;

class Solution {
    
    public int compute(int[] nums, int[][] dp, int low, int high){
        if(low> high){
            return 0;
        }
        if(low== high){
            return nums[low];
        }
        if(dp[low][high]!= 0){
            return dp[low][high];
        }
        dp[low][high]= Math.max(Math.max(Math.max(nums[low] + compute(nums, dp, low+2, high), nums[high]               + compute(nums, dp, low, high-2)), compute(nums, dp, low+1, high)), compute(nums, dp, low,                   high-1));
        return dp[low][high];
    }
    
    public int rob(int[] nums) {
        int n= nums.length;
        int[][] dp= new int[n][n];
        dp[0][n-1]= compute(nums, dp, 0, n-1);
        return dp[0][n-1];
    }
}


//OPTIMAL
class Solution2 {
    
    public int rob(int[] nums){
        int[] dp= new int[nums.length];
        if(nums.length== 0){
            return 0;
        }
        if(nums.length== 1){
            return nums[0];
        }
        if(nums.length== 2){
            return Math.max(nums[0], nums[1]);
        }
        dp[0]= nums[0];
        dp[1]= nums[1];
        dp[2]= nums[0] + nums[2];
        for(int i=3; i<nums.length; i++){
            dp[i]= nums[i] + Math.max(dp[i-2], dp[i-3]);
        }
        return Math.max(dp[nums.length-1], dp[nums.length-2]);
    }
    
}