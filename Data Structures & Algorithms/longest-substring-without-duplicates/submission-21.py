class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        hm = {}
        ans = 0
        while r < n:
            if s[r] not in hm:
                hm[s[r]] = r
            else :
                l = max(l,hm[s[r]]+1)
                hm[s[r]] = r
            ans = max(ans, r-l+1)
            r += 1
        if len(hm) == n:
            return n

        return ans


        