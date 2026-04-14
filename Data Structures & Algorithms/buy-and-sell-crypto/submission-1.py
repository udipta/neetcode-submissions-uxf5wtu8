class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # buy = 0
        # for sell in range(len(prices)):
        #     if prices[sell] > prices[buy]:
        #         max_profit = max(max_profit, prices[sell] - prices[buy])
        #     else:
        #         buy = sell
        # return max_profit
        min_price = prices[0]
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] < min_price:
                min_price = prices[right]
                left += 1

            max_profit = max(max_profit, prices[right] - min_price)
        return max_profit
