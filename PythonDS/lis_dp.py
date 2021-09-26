#problem link: https://leetcode.com/problems/longest-increasing-subsequence/submissions/
#problem statement: longest increasing subsequence in array dp

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [1]*n
        for i in range(1,n):
            for j in range(i):
                if(nums[i]> nums[j]):
                    dp[i]= max(dp[i], 1+dp[j])
        return max(dp)