class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      u = set(nums)
      ans = {}
      for i in u:
        ans[nums.count(i)] = i

      return ans[1]

      return ""
        