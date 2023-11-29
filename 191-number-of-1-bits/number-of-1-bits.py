class Solution:
    def hammingWeight(self, n: int) -> int:
        #print(bin(n))
        x = bin(n)
        m = [i for i in str(x)]
        return m.count('1')