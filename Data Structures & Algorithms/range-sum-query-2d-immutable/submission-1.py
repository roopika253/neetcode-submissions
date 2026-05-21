class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows= len(matrix)
        columns = len(matrix[0])
        self.row_matrix = [[0]*columns for i in range(rows)]
        for r in range(rows):
            for c in range(columns):
                if c > 0:
                    self.row_matrix[r][c] += self.row_matrix[r][c-1] + matrix[r][c]
                else :
                    self.row_matrix[r][c] = matrix[r][c]
        self.sum_matrix = [[0]*columns for i in range(rows)]
        for i in range(columns):
            for j in range(rows):
                if j > 0:
                    self.sum_matrix[j][i] += self.sum_matrix[j-1][i] + self.row_matrix[j][i]
                else :
                    self.sum_matrix[j][i] = self.row_matrix[j][i]



        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1-1 >= 0:
            if col1-1 >= 0:
                return self.sum_matrix[row2][col2] - self.sum_matrix[row2][col1-1] - self.sum_matrix[row1-1][col2] + self.sum_matrix[row1-1][col1-1]
            else :
                return self.sum_matrix[row2][col2] - self.sum_matrix[row1-1][col2]
        else :
            if col1-1 >= 0:
                return self.sum_matrix[row2][col2] - self.sum_matrix[row2][col1-1] 
            else:
                return self.sum_matrix[row2][col2] 


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)