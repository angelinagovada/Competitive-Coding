class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      u = set(nums)
      for i in u:
        x = nums.count(i)
        if x==1:
          print(nums)
          return i

      return ""
        