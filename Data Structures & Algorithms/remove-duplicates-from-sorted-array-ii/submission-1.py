class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        while r < n:
            if r < 2 or (nums[l-2]!=nums[r]):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l