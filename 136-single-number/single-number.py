class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      u = set(nums)
      for i in u:
        x = nums.count(i)
        if x==1:
          print(nums)
          return i

          '''
        else:
          #nums.remove(i)
          nums = list(filter(lambda a: a != i, nums))

          print(nums)
          '''

      return ""
        