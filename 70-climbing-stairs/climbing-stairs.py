class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1

        #We compute n-1 values, so range is from 0 to n-1
        for i in range(n):
            temp = two
            two = one + two
            one = temp

        return one

            

    '''
    one     two     a       b       c
    1       1       one+two two+a   a+b


    a = one+two
    b = a+two
    '''
            
        