class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ''' BRUTE Force '''

        ans = 0
        n = len(nums)
        k,l=0,0
        for i in range(n):
            for j in range(i+1,n):
                if(ans < nums[i]*nums[j]):
                    k,l = i,j
                    ans = max(ans, nums[i]*nums[j])

        return (nums[k]-1) * (nums[l]-1)

        