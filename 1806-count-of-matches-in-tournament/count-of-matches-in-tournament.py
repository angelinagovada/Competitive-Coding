class Solution:
    def numberOfMatches(self, n: int) -> int:
        c = 0
        while(n!=1):

            if(n%2!=0):
                n = n//2 
                c = c+n 
                n = n + 1
                #print(n)
            else:
                n = n//2 
                c = c+n
                #print(n)
                
        
        return c