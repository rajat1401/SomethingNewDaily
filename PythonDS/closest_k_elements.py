#link: https://leetcode.com/problems/find-k-closest-elements/submissions/
#statement: k closest elements to integer x from sorted array.

class ClosestK:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minindex= -1
        minn= 1000000000
        n= len(arr)
        for i in range(n):
            if(abs(arr[i]-x)< minn):
                minn= abs(arr[i]-x)
                minindex=i
        low= minindex-1
        high=minindex+1
        op= [arr[minindex]]
        count= 1
        while(low>= 0 and high<n and count< k):
            if(abs(arr[low]-x)< abs(arr[high]-x)):
                op.append(arr[low])
                low-= 1
            elif(abs(arr[low]-x)> abs(arr[high]-x)):
                op.append(arr[high])
                high+= 1
            else:
                if(arr[low]< arr[high]):
                    op.append(arr[low])
                    low-= 1
                else:
                    op.append(arr[high])
                    high+= 1
            count+= 1
        while(low>= 0 and count< k):
            op.append(arr[low])
            low-= 1
            count+= 1
        while(high< n and count< k):
            op.append(arr[high])
            high+= 1
            count+= 1
        op.sort()
        return op