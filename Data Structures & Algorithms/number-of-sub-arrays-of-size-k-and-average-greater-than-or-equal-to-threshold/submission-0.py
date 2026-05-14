class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        totalSum = 0
        ans = 0
        for i in range(k):
            totalSum += arr[i]
        avg = totalSum/k
        if avg >= threshold:
            ans += 1
      
     
        for i in range(k,n):
            totalSum += arr[i] - arr[i-k]
            
            avg = totalSum/k
            
            if avg >= threshold:
               
                ans += 1
        return ans


        