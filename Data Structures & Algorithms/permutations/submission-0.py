class Solution:
    def helper(self, nums, temp, used):
        if len(temp) == len(nums):
            self.ans.append(temp[:])
            return
        for i in range(len(nums)):
            if used[i] == 0:
                temp.append(nums[i])
                used[i] = 1
                self.helper(nums, temp , used)
                used[i] = 0
                temp.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        used = [0]*len(nums)
        self.helper(nums, [] , used)
        return self.ans
        