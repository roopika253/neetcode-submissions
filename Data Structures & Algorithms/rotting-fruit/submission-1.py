class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_fruits = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh_fruits += 1
        if fresh_fruits == 0:
            return 0
        time = -1
      
        dx = [-1, 0 , 1, 0]
        dy = [0 , -1 , 0 ,1]
        while queue:
            n = len(queue)
            time += 1
           
            for _ in range(n):
               
                indices = queue.popleft()
                i = indices[0]
                j = indices[1]
                for d in range(4):
                    nr = i + dx[d]
                    nc = j + dy[d]
                    print(nr,nc)
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append([nr,nc])
                        fresh_fruits -= 1

        if fresh_fruits == 0:
            return time
        return -1

        