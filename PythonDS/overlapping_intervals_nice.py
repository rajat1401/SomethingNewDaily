#problem link: https://leetcode.com/problems/non-overlapping-intervals/submissions/
#problem statement: find min intervals to be removed to have no overlap

class Intervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        print (intervals)
        count= 0
        low= 1
        end= intervals[0][1]
        n= len(intervals)
        while(low< n):
            if(intervals[low][0]< end):
                count+= 1
                end= min(end, intervals[low][1])
            else:
                end= intervals[low][1]
            low+= 1
        return count
            