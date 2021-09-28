#problem link: https://leetcode.com/problems/trapping-rain-water/submissions/
#problem statement: oh you know this!

class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        if(n== 1):
            return 0
        left= [-1]*n
        right= [-1]*n
        left[0]= height[0]
        right[n-1]= height[n-1]
        for i in range(1,n):
            left[i]= max(height[i], left[i-1])
        for i in range(n-2, -1, -1):
            right[i]=  max(right[i+1], height[i])
        summ= 0
        for i in range(1,n-1):
            summ+= max(0, min(left[i], right[i])-height[i])
        return summ