class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        r = 0
        l = 0
        prev = ""
        ans = 0
        while r < n-1 and l <= r:
            if arr[r+1] > arr[r]:
                if prev == "<" or prev == "":
                    prev = ">"
                else :
                    prev = ">"
                    ans = max(ans , r-l+1)
                    l = r
            elif arr[r+1] < arr[r]:
                if prev == ">" or prev == "":
                    prev = "<"
                else :
                    prev = "<"
                    ans = max(ans ,r-l+1)
                    l = r
            else :
                ans = max(ans ,r-l+1)
                l = r + 1
            r += 1
        ans = max(ans, r-l+1)

        
        return ans