class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b = 0
        s = 1
        max_profit = 0
        while s < n:
            if prices[s] > prices[b]:
                max_profit = max(max_profit, prices[s]-prices[b])
            else :
                b = s
            s += 1
        return max_profit

        