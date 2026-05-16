class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0] , nums[0]
        currMax, currMin = nums[0] , nums[0]
        total = nums[0]
        for n in nums[1:]:
            currMax = max(currMax+n , n)
            currMin = min(currMin+n , n)
            globalMax =max(globalMax , currMax)
            globalMin = min(globalMin , currMin)
            total += n
        return max(globalMax , total-globalMin) if globalMax > 0 else globalMax