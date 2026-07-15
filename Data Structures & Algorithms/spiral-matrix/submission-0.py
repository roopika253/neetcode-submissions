class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        left = 0
        right = c-1
        top = 0
        bottom = r-1
        ans = []
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if not (top <= bottom and left<=right):
                continue
            for i in range(right , left-1 , -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top-1 , -1):
                ans.append(matrix[i][left])
            left += 1
        return ans

        