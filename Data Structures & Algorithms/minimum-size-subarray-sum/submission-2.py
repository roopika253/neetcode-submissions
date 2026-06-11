class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        ans = n
        tmp = 0
        if sum(nums) < target:
            return 0
        while r < n:
            tmp += nums[r]
            while tmp >= target:
                ans = min(ans,r-l+1)
                tmp -= nums[l]
                l += 1
            r += 1
        return ans


        