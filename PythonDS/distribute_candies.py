#problem link: https://leetcode.com/problems/distribute-candies/submissions/
#problem statement: bleh

class candies:
    def distributeCandies(self, candyType: List[int]) -> int:
        dictt= {}
        for ctype in candyType:
            dictt[ctype]= 1
        return min(len(dictt), len(candyType)//2)