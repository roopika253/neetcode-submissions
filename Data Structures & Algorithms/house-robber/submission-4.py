class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2,n+1):
            take = nums[i-1] + dp[i-2]
            not_take = dp[i-1]
            dp[i] = max(take,not_take)
        return dp[n]
        