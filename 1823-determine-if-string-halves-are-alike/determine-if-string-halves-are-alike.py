class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ''' Brute Force '''

        n =len(s)
        s1 = s[:n//2]
        s2 = s[n//2:]

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        c1,c2=0,0
        for i in s1:
            if(i in vowels):
                c1+=1

        for j in s2:
            if(j in vowels):
                c2+=1


        return c1==c2
            



        