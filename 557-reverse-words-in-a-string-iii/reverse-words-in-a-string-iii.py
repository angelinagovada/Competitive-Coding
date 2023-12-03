class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split(" ")
        ans= s1[0][::-1]

        for i in range(1,len(s1)):
            ans=ans+" "+s1[i][::-1]

        #print(ans)
        return ans

        