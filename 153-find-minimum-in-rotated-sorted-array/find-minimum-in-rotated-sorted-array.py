class Solution:
    def findMin(self, nums: List[int]) -> int:
        #nums=[3,4,5,1,2]

        N=len(nums)
        res = nums[0]
        left = 0
        right = N-1
        mid = N//2
        #print(mid)
        #Binary(first,last,nums)

        if(nums[right]>=nums[0]):
            return nums[0]

        # nums[mid]>nums[mid+1] or nums[mid-1] <nums[mid]
        while ( right>=left):
            if (nums[mid-1]>nums[mid]):
                return nums[mid]
            if (nums[mid]>nums[mid+1]):
                return nums[mid+1]
            
            if (nums[mid]>nums[left] and nums[mid]>nums[right]):
                left = mid+1
            else:
                right = mid-1
            print((left+right)//2)
            mid=(left+right)//2
            print(mid)
            res=min(res,nums[mid])

        return (res)

