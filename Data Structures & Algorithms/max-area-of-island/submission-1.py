class Solution:
    def helper(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == 0 or (grid[r][c] == "#"):
            return 0
        grid[r][c] = "#"
        dx = [-1, 0, 1, 0]
        dy = [0, -1 , 0, 1]
        area = 1
        for d in range(4):
            area += self.helper(grid, r+dx[d], c+dy[d])
        return area
       


        
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] :
                    ans = max(ans,self.helper(grid,i,j))
        return ans


        