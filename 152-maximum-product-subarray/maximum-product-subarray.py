class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        maxProd = 1
        minProd = 1
        #currProd = 1
        res = max(nums)

        for i in nums:
            temp = minProd*i
            minProd = min(minProd*i, maxProd*i, i)
            #print(minProd)
            maxProd = max(maxProd*i, temp, i)
            #print(maxProd)
            res = max(res, maxProd)
            #print(res)

        return res

        