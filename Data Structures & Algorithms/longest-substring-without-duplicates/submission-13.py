class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        r = 0
        hm = {}
       
        if s == " ":
            return 1

        while l < n and r < n:
            if s[r] not in hm:
                hm[s[r]] = r
            else :
                l = max(l,hm[s[r]]+1)
                hm[s[r]] = r
           
            ans = max(ans,r-l+1)
            r += 1
                
        if len(hm) == n:
            return n
        return ans
        