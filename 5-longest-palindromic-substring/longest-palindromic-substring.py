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

        '''

        n = len(s)
        i = j = n//2
        
        if(s==s[::-1]):
            return s
        elif(n%2!=0):
            while(j<n and i!=0 and s[i]==s[j]):
                i=i-1
                j=j+1
                if(s[i]!=s[j]):
                    return s[i+1:j]
        else:
            i=i-1
            while(j<n and i!=0 and s[i]==s[j]):
                i=i-1
                j=j+1
                if(s[i]!=s[j]):
                    return s[i+1:j]

        return s[0]

        '''

                
            

            





    
        

        


    