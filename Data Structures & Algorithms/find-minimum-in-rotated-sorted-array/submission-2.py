class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        res = 1000
        while l <= h:
            if nums[l] < nums[h]:
                res = min(res,nums[l])
                break
            m = (l+h)//2
            res = min(res,nums[m])
            if nums[l] <= nums[m]:
                l = m+ 1
            else:
                h = m-1
        return res