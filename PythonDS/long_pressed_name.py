#problem link: https://leetcode.com/problems/long-pressed-name/submissions/
#problem statement: some character might get long pressed. given name and typed, return true if typed -> name.

class LongPressedName:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1= 0
        ptr2= 0
        while(ptr1< len(name)):
            count1= 1
            while(ptr1+1< len(name) and name[ptr1+1]== name[ptr1]):
                count1+= 1
                ptr1+= 1
            count2= 0
            while(ptr2< len(typed) and name[ptr1-count1+1]== typed[ptr2]):
                count2+= 1
                ptr2+= 1
            # print (ptr1, ptr2, count1, count2)
            if(count2< count1):
                return False
            ptr1+= 1
        if(ptr2== len(typed)):
            return True
        return False
            
            