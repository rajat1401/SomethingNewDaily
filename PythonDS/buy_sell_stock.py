#problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#problem statement: buy sell once maximise profit, if can't profit return 0

def maxProfit(prices):
    maxprofit= 0
    minprice= float('inf')
    n= len(prices)
    for i in range(n):
        if(prices[i]< minprice):
            minprice= prices[i]
        if(prices[i] - minprice> maxprofit):
            maxprofit= prices[i] - minprice    
    return maxprofit

arr= list(map(int, input().split()))
print (maxProfit(arr))