#problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#problem statement: buy sell once maximise profit, if can't profit return 0

def maxProfit(prices):
    maxprofit= 0
    minprice= float('inf')
    n= len(prices)
    for j in range(n):
        if(prices[j]< minprice):
            minprice= prices[j]
        if(prices[j] - minprice> maxprofit):
            maxprofit= prices[j] - minprice    
    return maxprofit

arr= list(map(int, input().split()))
print (maxProfit(arr))