#problem link: https://leetcode.com/problems/valid-parentheses/submissions/
#problem statement: string has valid parenthesis or not? classic stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for char in s:
            if(char== '(' or char== '{' or char== '['):
                stack.insert(0, char)
            else:
                if((char== ')' and stack and stack[0]== '(') or (char== '}' and stack and stack[0]=='{') or (char==']' and stack and stack[0]=='[')):
                    stack.pop(0)
                else:
                    return False
        if(stack):
            return False
        return True