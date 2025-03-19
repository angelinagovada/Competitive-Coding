class Solution:
    def hammingWeight(self, n: int) -> int:
        n1 = bin(n)
        res=0
        for i in n1:
            if i=='1':
                res+=1

        return res

