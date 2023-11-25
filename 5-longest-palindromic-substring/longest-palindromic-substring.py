class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans={}
        n = len(s)

        for i in range(n):
            for j in range(i,n):
                s1 = s[i:j+1]
                if(s1 == s1[::-1]):
                    ans[len(s1)]=s1

        
        print(ans)

        return ans[max(ans)]


    
        

        


    