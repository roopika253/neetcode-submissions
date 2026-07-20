import heapq , collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u,v,w in times:
            adjList[u].append([v,w])

        visited = set()
        ans = 0
        
        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (0 , k))

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            ans = max(ans, weight)
            visited.add(node)
            for v,w in adjList[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (weight+w, v))
                
        return ans if len(visited) == n else -1
        
            


     
