class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ''' BRUTE FORCE kinda'''

        if(len(s)==len(t)):
            t1 = [i for i in t]
            print(t1)

            for j in s:
                if j in t1:
                    t1.remove(j)
                else:
                    return False
                
        else:
            return False


        return True

        

        #CAN USE HASH MAP 




        