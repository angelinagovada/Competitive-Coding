class Solution:
    def removeVowels(self, s: str) -> str:
        ans =""
        vowels = ['a','e','i','o','u']
        
        for i in s:
            if i not in vowels:
                ans = ans+i

        return ans
        