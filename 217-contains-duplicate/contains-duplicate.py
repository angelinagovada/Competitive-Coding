class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        ans = False
        HashMap = {}

        for i in nums:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] +=1

        if(max(HashMap.values())>=2):
            print(max(HashMap))
            ans = True
        
        return ans

        