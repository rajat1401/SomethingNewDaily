#problem link: https://leetcode.com/problems/container-with-most-water/submissions/
#problem statement: like tapping rainwater but with spaces between buildings. 2 ptr approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        maxarea= 0
        low= 0
        high= n-1
        while(low< high):
            area= min(height[low],height[high])*(high-low)
            maxarea= max(maxarea, area)
            
            if(height[low]> height[high]):
                high-= 1
            else:
                low+= 1
        return maxarea