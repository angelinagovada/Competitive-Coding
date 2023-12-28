class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        Count0 = 0
        Count1 = 0
        ans = 0

        for i in range(N-1):
            Count0 = s[:i+1].count("0")
            Count1 = s[i+1:].count("1")

            print(Count0)
            print(Count1)

            ans = max(ans, Count0+Count1)

            


        return ans

        
        