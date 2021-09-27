#problem link: https://leetcode.com/problems/bulls-and-cows/submissions/
#problem statement: kinda lame

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n= len(secret)
        bulls= 0
        secleft= ""
        geleft= ""
        for i in range(n):
            if(secret[i]== guess[i]):
                bulls+= 1
            else:
                secleft+= secret[i]
                geleft+= guess[i]
        cows= 0
        guessdigits= [0]*10
        for i in range(len(geleft)):
            guessdigits[int(geleft[i])]+= 1
        for ch in secleft:
            if(guessdigits[int(ch)]> 0):
                cows+= 1
                guessdigits[int(ch)]-= 1
        return str(bulls) + "A" + str(cows) + "B"
        