from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        ans = []
        l = 0
        r = 0
        while r < n:
            if dq and l > dq[0]:
                dq.popleft()
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
          
            if r+1 >= k:
                ans.append(nums[dq[0]])
                l+= 1
           
            r += 1
        return ans
        