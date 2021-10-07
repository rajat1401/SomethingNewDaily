#problem link: https://leetcode.com/problems/lemonade-change/submissions/
#problem statement: you know this

class Lemonade:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins=[0]*2
        for i in range(len(bills)):
            if(bills[i]== 5):
                coins[0]+= 1
            elif(bills[i]== 10):
                coins[1]+= 1
                coins[0]-= 1
            else:
                if(coins[1]>= 1):
                    coins[1]-= 1
                else:
                    coins[0]-= 2
                coins[0]-= 1
            
            if(coins[0]< 0 or coins[1]< 0):
                return False
        return True
                