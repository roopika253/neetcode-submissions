class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        h = rows-1
        row = -1
        while l <= h:
            m = (l+h)//2
           
            if matrix[m][0] <= target <= matrix[m][columns-1]:
                row = m
                break
            elif matrix[m][0] < target:
                l = m + 1
            else :
                h = m - 1
       

        low = 0
        high = columns -1
        while low<=high:
            mid = (low+high)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                high = mid -1
            else :
                low = mid + 1
        return False
        