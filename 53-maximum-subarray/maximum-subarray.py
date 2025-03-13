class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        maxSum=-10000
        currSum = 0

        if(N==1):
            return nums[0]
        else:
            for i in range(N):
                if(currSum<0):
                    currSum=0
                    
                currSum +=nums[i]
                maxSum = max (maxSum,currSum)

            return  maxSum