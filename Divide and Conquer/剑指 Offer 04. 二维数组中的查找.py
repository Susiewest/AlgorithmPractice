和240题一样的
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        r, c = row-1, 0
        while 0<=r<row and 0<=c<col:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                r-=1
            elif matrix[r][c]<target:
                c+=1
        return False
执行用时：56 ms, 在所有 Python3 提交中击败了25.69%的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了10.35%的用户
