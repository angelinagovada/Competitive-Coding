class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set=set(nums)
        x = {nums.count(x):x for x in nums_set}
        print(x)
        return x[max(x)]
        
        