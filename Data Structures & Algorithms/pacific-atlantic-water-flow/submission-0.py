from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = deque()
        atlantic = deque()
        
        pac = [[False] * cols for i in range(rows)]
        atl = [[False] * cols for i in range(rows)]



        for i in range(cols):
            pacific.append([0,i])
            atlantic.append([rows-1,i])
            pac[0][i] = True
            atl[rows-1][i] = True
        
        for i in range(rows):
            pacific.append([i,0])
            atlantic.append([i,cols-1])
            pac[i][0] = True
            atl[i][cols-1] = True

        directions = [[-1,0] , [0,1] , [1, 0], [0, -1]]

      
        def bfs(visited, source):
            while source:
                indices = source.popleft()
                r = indices[0]
                c = indices[1]
               
                for d in range(4):
                    nr = r + directions[d][0]
                    nc = c + directions[d][1]
                    if nr < 0 or nr >=rows or nc <0 or nc >=cols or visited[nr][nc] == True or heights[nr][nc] < heights[r][c] :
                        continue
                    source.append([nr,nc])
                    visited[nr][nc] = True

        

        bfs(pac, pacific)
        bfs(atl, atlantic)

        res = []

        for i in range(rows):
            for j in range(cols):
                if atl[i][j] and pac[i][j]:
                    res.append([i,j])
        
        return res




        