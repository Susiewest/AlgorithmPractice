#要常数空间的解，这个方法好像是o(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        mark_row=set()
        mark_col=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    mark_row.add(i)
                    mark_col.add(j)
        for i in range(row):
            for j in range(col):
                if i in mark_row or j in mark_col:
                    matrix[i][j]=0
        

'''执行用时：
40 ms, 在所有 Python3 提交中击败了98.36%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了22.43%的用户'''
