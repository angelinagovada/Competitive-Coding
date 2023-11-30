class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans = 0
        c = 1
        if(sum(nums)==0):
            return 0
        for i in range(len(nums)-1):
            if(nums[i]==1 and nums[i+1]==1):
                c=c+1
                ans = max(ans,c)            
            else:
                c=1

        ans = max(ans,c)


        return ans


        