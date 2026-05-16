class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hm = {}
        for i in range(n):
            if nums[i] not in hm:
                hm[nums[i]] = i
            else :
                index = hm[nums[i]]
                if i-index <= k:
                    return True
                hm[nums[i]] = i
       
        return False
        