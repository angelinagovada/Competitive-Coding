class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ''' BRUTE FORCE - FAILED THOUGH a.k.a. TimeOut

        u = []
        n = len(s)
        length = 0
        i,j=0,0
        while j<n:
            if s[j] not in u:
                u.append(s[j])
                j=j+1
            else:
                length = max(length, len(s[i:j]))
                i=i+1

        return length

        '''

        ### Using Sliding Window Technique

        ans = 0
        l = 0

        window = set()
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l = l + 1

            window.add(s[r])
            ans = max(ans, r-l+1)

        return ans




        