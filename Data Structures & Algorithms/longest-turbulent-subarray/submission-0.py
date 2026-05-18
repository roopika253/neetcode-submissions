class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            c = 1
            for j in range(i,n-1):
                if j%2 == 0 :
                    if arr[j+1] > arr[j]:
                        c += 1
                    else :
                        break
                else :
                    if arr[j+1] < arr[j]:
                        c += 1
                    else :
                        break
            ans = max(c,ans)
        for i in range(n):
            c = 1
            for j in range(i,n-1):
                if j%2 == 0 :
                    if arr[j+1] < arr[j]:
                        c += 1
                    else :
                        break
                else :
                    if arr[j+1] > arr[j]:
                        c += 1
                    else :
                        break
            ans = max(c,ans)
        return ans