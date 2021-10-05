#problem link: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
#problem statement: min length of subarray with sum>= target

class minSubarray:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low= 0
        high= 0
        n= len(nums)
        cursum= 0
        minlen= n+1
        while(low<=high and high< n):
            while(high< n and cursum< target):
                cursum+= nums[high]
                high+= 1        
            while(low< high and cursum>= target):
                minlen= min(minlen, high-low)
                cursum-= nums[low]
                low+= 1
        if(minlen> n):
            return 0
        return minlen
            
                