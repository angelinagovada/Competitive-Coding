class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        total = 0
        ans=nums[0]

        #print(nums)         
           
        for i in range(len(nums)):
            if(total<0):
                total=0
                #total = nums[i]   #wrong
            
            total = total + nums[i]
            ans = max(ans, total)
        
        #print(nums[i:])
        #print("total",total)
        #print("ans",ans)0


        return ans
