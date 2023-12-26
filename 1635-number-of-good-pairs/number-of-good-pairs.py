class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #BRUTE FORCE
        n = len(nums)
        c = 0

        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    c = c+1
        
        return c



        