class Solution:
    def helper(self, index, nums, temp):
        if index >= len(nums):
            self.ans.append(temp[:])
            return
        self.helper(index + 1, nums, temp+[nums[index]])
        self.helper(index + 1, nums, temp)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(0, nums , [])
        return self.ans

        