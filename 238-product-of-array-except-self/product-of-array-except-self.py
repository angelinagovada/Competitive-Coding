class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
                1   2   3   4
        prefix  1   2   3   4
        pre     1   2   6   24
        post   24   24  12  4

        '''

        pre=list(nums)
        #print("pre",pre)
        post=list(nums)
        x=1
        for i in range(len(nums)):
            x=x*nums[i]
            pre[i]=x

        print(pre)
        x=1
        #print("before j nums",nums)
        for j in range(len(nums)-1,-1,-1):
            #print("nums",nums)
            #print("j",j)
            x=x*nums[j]
            post[j]=x
            #print("x",x)

        print(post)
        
        ans = list(post)

        for k in range(len(nums)):
            if(k==0):
                ans[k] = post[1]
            elif(k==len(nums)-1):
                ans[k] = pre[k-1]
            else:
                ans[k]=pre[k-1]*post[k+1]
            
        
        return ans

''' Sample test case: 

    nums    2  3  4
    pre     2  6  24
    post    24 12  4

    ans     12  8  6

    '''




        