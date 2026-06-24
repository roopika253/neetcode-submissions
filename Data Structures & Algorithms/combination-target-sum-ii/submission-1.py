class Solution:
    def helper(self,nums, target, index, tmp):

        if target == 0:
            self.ans.append(tmp) 
            return

        if index >= len(nums) or target < 0:
            return

        next_index = index+1

        for i in range(index+1 , len(nums)):
            if nums[i] == nums[index]:
                next_index += 1
        
        self.helper(nums, target-nums[index] , index+1 , tmp+[nums[index]])
        self.helper(nums, target , next_index , tmp)
        


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans= []
        self.helper(sorted(candidates), target , 0, [])
        return self.ans
        