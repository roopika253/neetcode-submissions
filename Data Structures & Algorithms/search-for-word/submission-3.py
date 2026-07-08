class Solution:
    def helper(self, r , c , i, j, index , target , board , vis):
        if i >=r or i < 0 or j >=c or j < 0 :
            return False
        if vis[i][j] == 0:
            if target[index] != board[i][j]:
                return False
            vis[i][j] = 1
        else:
            return False
        if index == len(target)-1:
            return True
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        for d in range(4):
            if self.helper(r , c, i+dx[d], j+dy[d] , index+1 , target , board, vis):
                return True
        vis[i][j] = 0
        return False
       
           
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        vis = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j]:
                    if self.helper(r,c,i,j,0, word , board ,vis):
                        return True
        return False
