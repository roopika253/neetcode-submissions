import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = [0]*27
        for i in tasks:
            hm[ord(i)-65] += 1
        maxheap = []
        for i in hm:
            if i:
                maxheap.append(-i)
        heapq.heapify(maxheap)
        q = deque() #[cnt, idletime]
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1+ heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time


        
        