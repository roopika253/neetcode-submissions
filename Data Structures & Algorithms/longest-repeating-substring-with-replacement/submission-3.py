class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in s:
            count = 0
            l = 0
            for j in range(n):
                if s[j] == i:
                    count += 1
                while (j-l+1) - count > k:
                    if s[l] == i:
                        count -= 1
                    l += 1
                ans = max(ans, j-l+1)
        return ans
