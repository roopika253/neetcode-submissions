import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        heap = []
        heapq.heapify(heap)
     
        for i in range(n):
            x = points[i][0]
            y = points[i][1]
            # Need not to take a square root because the order of the distances remain same
            # with or without square roor
            d = x*x + y*y  
            heapq.heappush(heap,(-d,[x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans



        