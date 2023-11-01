class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            balance = target - nums[i]
            if (balance in ans):
                return ([i,ans[balance]])
            ans[nums[i]] = i 
