#problem link: https://leetcode.com/problems/maximum-subarray/
#problem statement: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubarray(arr):
    papasum= -400000000000
    cursum= papasum
    for i in range(len(arr)):
        cursum= max(arr[i], cursum+arr[i])
        papasum= max(papasum, cursum)
    return papasum

arr= list(map(int, input().split()))
print (maxSubarray(arr))