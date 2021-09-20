#problem link: https://leetcode.com/problems/repeated-substring-pattern/submissions/
#problem statement: check if string has a repeated substring or not

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cur= 1
        n= len(s)
        while(cur<= n//2):
            if(n%cur== 0):
                flag= True
                pattern= s[:cur]
                for i in range(cur,n,cur):
                    if(s[i:i+cur]!= pattern):
                        flag= False
                        break
                if(flag): return flag
            cur+= 1
        return False

s= 'babbabbab'
a= Solution()
print (a.repeatedSubstringPattern(s))