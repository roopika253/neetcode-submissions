class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hm = [0]*26
        l = 0
        r = 0
        ans = 0
        while l < n and r < n:
            hm[ord(s[r]) - 65] += 1
            maxfreq = max(hm)
            length = r-l+1
            while length - maxfreq > k :
                hm[ord(s[l]) - 65] -= 1
                l += 1
                length = r-l+1
                maxfreq = max(hm)
            ans = max(ans, length)
            r += 1
        return ans
