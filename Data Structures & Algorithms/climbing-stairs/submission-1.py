class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fn(indx):
            if indx == 0:
                return 1
            if indx == 1:
                return 1
            if dp[indx] != -1:
                return dp[indx]
            dp[indx] = fn(indx-1) + fn(indx-2)
            return dp[indx]
        return fn(n)


        