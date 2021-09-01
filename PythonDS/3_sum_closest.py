#problem link: https://leetcode.com/problems/3sum-closest/
#problem statement: given an array and integer target, find 3 integers in array with sum closest to target

def closestSum(nums, target):
    mindiff= float('inf')
    closestsum= float('inf')
    nums.sort()
    n= len(nums)
    for i in range(n-2):
        low= i+1
        high= n-1
        while(low< high):
            if(abs(nums[i]+nums[low]+nums[high] - target)< mindiff):
                mindiff= abs(nums[i]+nums[low]+nums[high] - target)
                closestsum= nums[i]+nums[low]+nums[high]
            if(nums[i]+nums[low]+nums[high] > target):
                high-= 1
            elif(nums[i]+nums[low]+nums[high] < target):
                low+= 1
            else:
                return target
    return closestsum


arr= list(map(int, input().split()))
target= int(input())
print  (closestSum(arr, target))
