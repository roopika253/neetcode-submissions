import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        hm = defaultdict(int)
        temp_sum = 0
        hm[0] =1 
        for i in range(n):
            temp_sum += nums[i]
            diff = temp_sum -k
            if diff in hm:
                c += hm[diff]
            hm[temp_sum] += 1

        return c
        