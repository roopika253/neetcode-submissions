class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = -10**9
       
        for i in range(n):
            currSum = 0
            for j in range(i,n+i):
                currSum += nums[j%n]
                maxSum = max(maxSum,currSum)
                if currSum < 0:
                    currSum = 0

        return maxSum