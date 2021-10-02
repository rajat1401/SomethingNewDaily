#problem link: https://leetcode.com/problems/powx-n/submissions/
#problem statement: calculate pow(x,n) precision upto 5 digits

class Solution:
    
    def calc(self,x,n):
        if(n== 1):
            return x
        a= self.calc(x,n//2)
        if(n%2== 1):
            return a*a*x
        else:
            return a*a
    
    def myPow(self, x: float, n: int) -> float:
        if(n== 0):
            return 1
        ans= self.calc(x,abs(n))
        if(n< 0):
            ans= 1/ans
        return (float("{:.5f}".format(ans)))

sol= Solution()
print (sol.myPow(2.1,3))