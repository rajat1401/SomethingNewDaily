#problem link: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
#problem statement: You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

class ClimbOneorTwo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        dp= [0]*len(cost)
        if(n== 1):
            return 0
        if(n== 2):
            return min(cost[0], cost[1])
        dp[0]= cost[0]
        dp[1]= cost[1]
        for i in range(2, n+1):
            if(i== n):
                return min(dp[i-1], dp[i-2])
            dp[i]= min(dp[i-1], dp[i-2]) + cost[i]
        return -1