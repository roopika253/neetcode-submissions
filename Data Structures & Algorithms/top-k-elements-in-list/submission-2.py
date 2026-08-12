from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        hp = []
        ans = []
        # heapq.heapify(hp) # making it heap
        for i in hm:
            heapq.heappush(hp , (hm[i], i))
            if len(hp) > k:
                heapq.heappop(hp)
        for i in range(k):
            ans.append( heapq.heappop(hp)[1])
        return ans
        