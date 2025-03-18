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

        if(nums[left]<nums[right]):
            return nums[left]
        else:
            while(right>left):
                if(nums[mid-1] > nums[mid]):
                    return nums[mid]
                elif(nums[mid] > nums[mid+1]):
                    return nums[mid+1]
                else:
                    if(nums[mid]>nums[left]):
                        left = mid+1
                    else:
                        right = mid-1

                    res = min (res,nums[mid])
                    mid = (left+right)//2

        return res

       

