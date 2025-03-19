class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [bin(i).count('1') for i in range(0,n+1)]
        #print(nums)
        return nums
        