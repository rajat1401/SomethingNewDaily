#problem link: https://leetcode.com/problems/car-pooling/submissions/
#problem statement: array [passangers, from, to] and capacity. trip possible or not?

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n= len(trips)
        q= []
        for i in range(n):
            heapq.heappush(q, [trips[i][1], trips[i][0]])
            heapq.heappush(q, [trips[i][2], -trips[i][0]])
        cur= 0
        while(q):
            a= heapq.heappop(q)
            cur+= a[1]
            if(cur> capacity):
                return False
        return True