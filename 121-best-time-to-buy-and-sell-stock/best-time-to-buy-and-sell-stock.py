class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        '''  TIME LIMIT EXCEEDED - BRUTE FORCE 
        profit=0

        for buy in range(len(prices)):
            sell=buy+1
            while(sell<len(prices)):
                if(prices[buy]<prices[sell] and p< prices[sell]-prices[buy]):
                    p = prices[sell]-prices[buy]
                sell=+1

        return profit

        '''

        buy, sell = 0, 1
        profit = 0

        while(sell<len(prices)):
            if(prices[sell]>prices[buy]):
                profit = max(profit,prices[sell]-prices[buy])
                sell = sell + 1
            else:
                buy  = sell
                sell = sell + 1
        return profit




        