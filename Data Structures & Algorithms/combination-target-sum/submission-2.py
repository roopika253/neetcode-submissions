class Solution:
    
    def helper(self, index, n, tmp, running_sum, nums, target):
        if index >= n or running_sum > target:
            return
        if running_sum == target:
            if tmp not in self.ans:
                self.ans.append(tmp)
                return
    
        self.helper(index, n, tmp+[nums[index]] , running_sum + nums[index], nums, target)
        self.helper(index+1, n, tmp, running_sum, nums, target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        self.helper(0, n, [], 0, nums, target)
        return self.ans

        