import collections
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        indx = 0
        for i in hm:
            nums[indx] = i
            indx += 1
        return len(hm)

        