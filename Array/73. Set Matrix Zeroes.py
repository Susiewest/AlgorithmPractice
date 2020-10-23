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

#o（1）解 注意！也有坑 那就是不要先处理第一行第一列 放在最后处理！顺序很重要 不然就会全变为0！
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_flag=False
        col_flag=False
        for i in range(row):
            if matrix[i][0]==0:
                #第一列有0
                col_flag=True
                break
        for j in range(col):
            if matrix[0][j]==0:
                row_flag=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        #为什么啊 这里之前写的range（row）就报错
        #哦！是因为 我们要先处理除了第一行第一列以外的 再处理第一行第一列
        #而写range(row)把第一行直接处理了，会导致第一行若有0则全变为0
        #第一行全0了 后面每个判断所在行/所在列标志位也会全满足 全改成0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if col_flag:
            for i in range(row):
                matrix[i][0]=0
        if row_flag:
            for j in range(col):
                matrix[0][j]=0
        
'''执行用时：
48 ms, 在所有 Python3 提交中击败了84.88%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了26.85%的用户'''
