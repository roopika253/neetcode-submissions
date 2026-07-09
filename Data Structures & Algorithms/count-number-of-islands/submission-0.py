class Solution:
    def helper(self,grid,i,j):
        if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]):
            return
        
        if grid[i][j] == "0" or grid[i][j] == "#":
            return

       
        grid[i][j] = "#"

        dx = [-1, 0 , 1, 0]
        dy = [0, -1, 0, 1]

        for d in range(4):
            ni = dx[d] + i
            nj = dy[d] + j
            self.helper(grid,ni,nj)



    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if grid[i][j] != "#":
                        ans += 1
                        self.helper(grid,i,j)
        return ans
        
        