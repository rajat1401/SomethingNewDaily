#problem link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#problem statement: given sorted array, return indices of elements that sum to a given target

def twoSum(nums, target):
    low= 0
    n= len(nums)
    high= n-1
    while(low< high):
        while(low< high and nums[low]+nums[high]< target):
            low+= 1
        while(low< high and nums[low]+nums[high]> target):
            high-= 1
        if(nums[low]+nums[high]== target):
            return [low+1, high+1]
    return [0,n-1]

nums= [2,7,11,15]
print (twoSum(nums,9))