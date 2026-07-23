import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for i in range(rows)]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        heap = [(grid[0][0],0,0)]
        heapq.heapify(heap)
        visited[0][0] = 1
        t = 0
        while heap:
            w,r,c = heapq.heappop(heap)
            t = max(t, w)
            if r == rows-1 and c == cols-1:
                return t
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >=rows or nc < 0 or nc >=cols or visited[nr][nc] == 1:
                    continue
                heapq.heappush(heap,(grid[nr][nc],nr,nc))
                visited[nr][nc] = 1
