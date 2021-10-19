#problem link: https://leetcode.com/problems/longest-mountain-in-array/
#problem statemennt: you know

class Mountain:
    def longestMountain(self, arr: List[int]) -> int:
        low= 0
        n= len(arr)
        maxx= 0
        while(low< n-2):
            tmp= low
            up= 0
            down= 0
            while(low+1< n and arr[low+1]> arr[low]):
                low+= 1
                up+= 1
            if(low== n-1):
                break
            while(low+1< n and arr[low+1]< arr[low]):
                low+= 1
                down+= 1
            if(up!= 0 and down!= 0):
                maxx= max(maxx, up+down+1)
            if(up== 0 and down== 0):
                low+= 1
        if(maxx>= 3):
            return maxx
        return 0
            