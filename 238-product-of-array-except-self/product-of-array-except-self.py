class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ####### pre, pos, res ########

        N = len(nums)
        pre = [1]*N
        pos = [1]*N
        res = [1]*N

        for i in range(1,N):
            pre[i]=pre[i-1]*nums[i-1]

        for k in range(N-2,-1,-1):
            pos[k]=pos[k+1]*nums[k+1]

        for j in range(N):
            res[j] = pre[j]*pos[j]

        return res
        

        '''  To reduce space omplexity  --- FAILEDDD 
        N = len(nums)
        res = [1]*N

        for i in range(1,N):
            res[i]=res[i-1]*nums[i-1]

        
        right = 1
        for k in range(N-2,-1,-1):
            res[k]=res[k]*right
            right = right*nums[i]

        return res
        '''




        
        