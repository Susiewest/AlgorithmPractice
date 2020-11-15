从左下角开始查找，等于就return，大于就抛弃掉这一行，小于就抛弃掉这一列，不断减小搜索空间，可称为减治
肯定不可能从左上角/右下角开始找，这样的话查找的数必然比当前元素大/小，没有办法缩小搜索的方向
可以用右上角开始，但在col初始化的时候，会出现matrix=[] 导致matrix[0]不存在的情况，要单独return一下

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)-1
        col = 0
        while(0<=row<len(matrix) and 0<=col<len(matrix[0])):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                col+=1
            elif matrix[row][col]>target:
                row-=1
        return False

执行用时：40 ms, 在所有 Python3 提交中击败了94.42%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了28.43%的用户

从右上角开始查找
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0])-1
        while(0<=row<len(matrix) and 0<=col<len(matrix[0])):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            elif matrix[row][col]>target:
                col-=1
        return False

执行用时：44 ms, 在所有 Python3 提交中击败了85.27%的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了44.26%的用户

