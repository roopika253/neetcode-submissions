from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        sources = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not(grid[i][j]):
                    sources.append([i,j])

        LAND = 2147483647
        
        directions = [[-1,0] , [0, 1] , [0, -1] , [1, 0]]
        distance = 0
        while sources:
            n = len(sources)
            distance += 1
            for i in range(n):
                top = sources.popleft()
                r = top[0]
                c = top[1]
                for i in range(4):
                    nr = r + directions[i][0]
                    nc = c + directions[i][1]
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == -1 or grid[nr][nc] == 0 or grid[nr][nc] != LAND:
                        continue
                    else :
                        grid[nr][nc] = distance
                        sources.append([nr,nc])
        
                   





        