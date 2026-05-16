class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        currSum = 0
        ans = n
        if sum(nums) < target:
            return 0
        while l < n and r < n:
            currSum += nums[r]
            if currSum >= target:
                print(l,r)
                ans = min(ans , r-l+1)
                l += 1
                r = l
                currSum = 0
            else :
                r += 1
        return ans
        


        