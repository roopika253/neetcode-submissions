class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = [0]*26
        n = len(s)
        l = 0
        r = 0
        ans = 0
        while l<n and r < n:
            hm[ord(s[r])- 65] += 1
            max_value = max(hm)
            length = r-l+1
            while length - max_value > k:
                hm[ord(s[l]) - 65] -= 1
                max_value = max(hm)
                l += 1
                length = r-l+1
            ans = max(ans, length)
            r += 1
        return ans



        