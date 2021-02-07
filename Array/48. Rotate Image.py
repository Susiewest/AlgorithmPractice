#转置和反转注意j的取值范围
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        #transpose
        for i in range(size):
            for j in range(i,size):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #reverse
        for i in range(size):
            for j in range(size//2):
                matrix[i][j],matrix[i][size-j-1]=matrix[i][size-j-1],matrix[i][j]
                
                
'''执行用时：
40 ms, 在所有 Python3 提交中击败了71.56%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了23.32%的用户'''

二刷，依然要注意transpose和inverse都不能从头遍历到尾，这样最后相当于没换。。。

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        #transpose
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        #reverse
        for i in range(size):
            for j in range(size//2):
                matrix[i][j], matrix[i][size-1-j] = matrix[i][size-1-j], matrix[i][j]
        return matrix

执行用时：36 ms, 在所有 Python3 提交中击败了81.12%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了37.42%的用户

