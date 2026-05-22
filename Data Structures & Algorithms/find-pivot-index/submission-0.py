class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0]*n
        ssum = [0]*n
        psum[0] = nums[0]
        ssum[n-1] = nums[n-1]
        for i in range(1,n):
            psum[i] = psum[i-1] + nums[i]
            ssum[n-i-1] = ssum[n-i] + nums[n-i-1]
        for i in range(n):
            if i+1 < n and psum[i]-nums[i] == ssum[i+1]:
                return i
            elif psum[n-1]-nums[n-1] == 0:
                return n-1
            
        return -1 
        