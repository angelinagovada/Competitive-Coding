class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        ans = []

        for k in nums:
            s=s+k
            ans.append(s)

        return ans
