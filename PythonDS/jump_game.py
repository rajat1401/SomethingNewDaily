#problem link: https://leetcode.com/problems/jump-game/submissions/
#problem statement: initially at first index, max jump length is value of array at that position. determine if reach last index


def canJump(nums):
    n= len(nums)
    if(n== 1):
        return True
    added= [False]*(n)
    q= []
    q.append([0, nums[0]])
    added[0]= True
    while(q):
        a= q.pop(0)
        for num in range(1,a[1]+1):
            if(a[0]+num== n-1):
                return True
            if(a[0]+num< n and not added[a[0]+num]):
                q.append([a[0]+num, nums[a[0]+num]])
                added[a[0]+num]= True
    return False

nums= [2,3,1,1,4]
print (canJump(nums))