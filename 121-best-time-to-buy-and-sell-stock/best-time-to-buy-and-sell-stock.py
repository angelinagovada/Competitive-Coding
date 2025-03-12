class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right= 1

        profit = 0

        for right in range(1, len(prices)):
            if (prices[right] < prices[left] ):
               left = right
                #right +=1 
            elif( profit < prices[right] - prices[left] ):
                profit = prices[right] - prices[left]
                #right += 1


        return profit




        