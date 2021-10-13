#problem link: https://leetcode.com/problems/maximum-number-of-eaten-apples/submissions/
#problem statement: you know this!

import heapq

class MaxEatenApples:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q= []
        n= len(apples)
        day= 0
        count= 0
        while(q or day< n):
            if(day< n and apples[day]> 0):
                heapq.heappush(q, [day+days[day], apples[day]])
            while(q and q[0][0]<= day):
                a= heapq.heappop(q)
            if(q):
                a= heapq.heappop(q)
                count+= 1
                a[1]-= 1
                if(a[1]> 0):
                    heapq.heappush(q, [a[0], a[1]])
            #print ("Day is: " + str(day) + " and count is: " +  str(count))
            day+= 1
        return count