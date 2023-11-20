import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #ans =-1

        dp = [sys.maxsize]*(amount+1)
        # 0 and 1 to amount stored in dp[]
        dp[0] = 0

        if(amount==0):
            return 0
        else:
            for i in range(len(dp)):
                for j in coins:
                    if(i-j)>=0:
                        dp[i] = min(dp[i], 1 + dp[i-j])

        if( dp[amount]!= sys.maxsize):
            return dp[amount]
        else:
            return -1
        