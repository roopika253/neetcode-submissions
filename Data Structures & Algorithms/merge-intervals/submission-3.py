class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        if n == 1:
            return intervals
        sorted_intervals = sorted(intervals)
        l1 = 0
        l2 = 1
        ans = [sorted_intervals[0]]



        while l2 < n:
            if sorted_intervals[l2][0] > ans[l1][1]:
                ans.append(sorted_intervals[l2])
                l1 += 1
            else :
                ans[l1][1] = max(ans[l1][1],sorted_intervals[l2][1])
            l2 += 1
        return ans
            

            



        