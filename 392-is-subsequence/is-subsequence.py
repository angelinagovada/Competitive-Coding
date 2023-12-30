class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = [ i for i in t]
        
        for j in s:
            #print("j: ",j)
            if (j not in t):
                return False
            else:
                k = t.index(j)
                t = t[k+1:]
                #print("t: ",t)

        return True
        