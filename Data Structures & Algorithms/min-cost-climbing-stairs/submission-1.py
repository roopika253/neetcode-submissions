class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        INT_MAX = 10**9
        dp = [-1]*(n+1)
        def fn(indx):
            if indx == 0 :
                return 0
            if indx == 1:
                return 0
            if dp[indx]!= -1:
                return dp[indx]
            fs = fn(indx-1) + cost[indx-1]
            ss = INT_MAX
            if indx-2 >= 0:
                ss = min(ss,fn(indx-2) + cost[indx-2])
            dp[indx] = min(fs,ss)
            return dp[indx]
        return fn(n)
        