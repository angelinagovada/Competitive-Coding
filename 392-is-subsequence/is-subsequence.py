class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t1=t
        res=True

        for i in s:

            if i in t1:
                x=t1.index(i)
                t1=t1[x+1:]
            else:
                res = False

        return res
