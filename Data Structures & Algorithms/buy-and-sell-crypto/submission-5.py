class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy =0
        # sell =1
        # profit=0
        # while sell<len(prices):
        #     if prices[buy]<prices[sell]:
        #         amt = prices[sell]-prices[buy]
        #         profit= max(profit,amt)
        #     else:
        #         buy=sell
        #     sell+=1
    
                

        # return profit

        buy =0
        sell = 1
        profit =0

        while sell<len(prices):
            if prices[buy]<prices[sell]:
                value = prices[sell]-prices[buy]
                profit=max(value,profit)

            else:
                buy =sell
            sell+=1
        
        return profit



























































