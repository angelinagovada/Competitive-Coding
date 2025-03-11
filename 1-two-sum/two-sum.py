class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans =[]
        HashMap = {}
        for i in range(len(nums)):
            if (target-nums[i] not in HashMap):
                HashMap[nums[i]] = i
            else:
                ans += [ HashMap[target-nums[i]], i]
        
        return ans