from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        sources = deque()
        visited = [[0] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i==0 or j == 0 or i == rows-1 or j == cols-1:
                    if board[i][j] == "O":
                        sources.append([i,j])
                        visited[i][j] = 1
                       

        directions = [[-1,0] , [0,1] , [1,0] , [0,-1]]
   

        while sources:
            indices = sources.popleft()
            r = indices[0]
            c = indices[1]
           
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or visited[nr][nc] or board[nr][nc] == "X":
                    continue
                sources.append([nr,nc])
                visited[nr][nc] = 1
        
 

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
        

        