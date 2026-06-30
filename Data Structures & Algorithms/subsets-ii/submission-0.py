class Solution:
    def helper(self, nums , temp , index):
        if index >= len(nums):
            if temp[:] not in self.ans:
                self.ans.append(temp[:])
            return
        temp.append(nums[index])
        self.helper(nums , temp , index+1)
        temp.pop()
        self.helper(nums , temp , index+1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(sorted(nums) , [] , 0)
        return self.ans
        