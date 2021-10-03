#problem link: https://leetcode.com/problems/two-sum/submissions/
#problem statement: given array, find index such sum of numbers equals target

class two_sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        llist= []
        for i in range(len(nums)):
            llist.append([i, nums[i]])
        llist= sorted(llist, key= lambda x: x[1])
        n= len(nums)
        low= 0
        high= n-1
        while(low< high):
            cursum= llist[low][1]+llist[high][1]
            if(cursum== target):
                return [llist[low][0], llist[high][0]]
            if(cursum< target):
                low+= 1
            else:
                high-= 1
        return []