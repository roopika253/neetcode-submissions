class Solution:
    def helper(self, nums , temp , index):
        if index >= len(nums):
            self.ans.append(temp[:])
            return
        temp.append(nums[index])
        self.helper(nums , temp , index+1)
        lastEle = temp.pop()
        while index < len(nums) and nums[index] == lastEle:
            index += 1
        self.helper(nums , temp , index)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(sorted(nums) , [] , 0)
        return self.ans
        