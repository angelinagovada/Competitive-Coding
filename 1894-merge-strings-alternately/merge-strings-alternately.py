class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        smaller = min(len1, len2)
        ans =""

        for i in range(smaller):
            ans = ans+word1[i]+word2[i]

        if(len1>len2):
            ans = ans+word1[i+1:]
        elif(len2>len1):
            ans = ans+word2[i+1:]

        return ans
