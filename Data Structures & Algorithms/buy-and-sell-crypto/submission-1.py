class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_array = [0]*n
        if n == 1:
            return 0
        max_array[-2] = prices[-1]
        for i in range(n-2):
            max_array[n-i-3] = max(prices[n-i-2],max_array[n-i-2])
        profit = 0
        for i in range(n-1):
           
            profit = max(profit,max_array[i]-prices[i])

        return profit


        