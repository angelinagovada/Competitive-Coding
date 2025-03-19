class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N+1):
            if i not in nums:
                return i
        