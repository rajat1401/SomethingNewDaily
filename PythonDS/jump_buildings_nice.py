#problem link: https://leetcode.com/problems/furthest-building-you-can-reach/submissions/
#problem statement: ladders and stairs. reach farthest building. 

import heapq

class FarthestBuilding:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q= []
        n= len(heights)
        for i in range(1,n):
            if(heights[i]> heights[i-1]):
                heapq.heappush(q, heights[i]-heights[i-1])
            if(len(q)> ladders):
                a= heapq.heappop(q)
                bricks-= a
                if(bricks< 0):
                    return i-1
        return n-1