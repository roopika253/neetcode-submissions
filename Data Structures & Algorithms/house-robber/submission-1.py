class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        
        def fn(indx):
            if indx == 0:
                return 0
            if indx == 1:
                return nums[0]
            if dp[indx] != -1:
                return dp[indx]
            dp[indx] = max(fn(indx-1) , nums[indx-1] + fn(indx-2))
            return dp[indx]
        return fn(n)
        