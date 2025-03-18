class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N-1
        mid = N//2
        res = -1

        if(N==1 and nums[0]==target):
            return 0

        while(right>left):
            if(nums[left]==target):
                return left
            elif(nums[mid]==target):
                return mid
            elif(nums[right]==target):
                return right
            else:
                # nums[mid]>nums[left] ---- means left to mid subarray is sorted
                if(nums[mid]>nums[left]):
                    if(target>nums[left] and target<nums[mid]):
                        right = mid-1
                    else:
                        left = mid+1
                # nums[mid]<nums[left] ---- means mid to right subarray is sorted
                else:
                    if(target<nums[right] and target>nums[mid]):
                        left = mid+1
                    else:
                        right = mid-1

            
            mid = (left+right)//2
        
        return res



         
        