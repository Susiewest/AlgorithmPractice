#这个题如果用寻路的方法做是不行滴。。。
'''  [ 1,  5,  9],
     [10, 11, 13],
     [12, 13, 15]  '''
#如果一直在右/下取较小值走到了9，就没法再回到第二行开头的10   
下面的方法，按值二分，而非传统的按有序数组下标二分
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        if k==1:
            return matrix[0][0]
        left = matrix[0][0]
        right = matrix[row-1][col-1]
        while left<=right:
            mid = (left+right)//2
            count, cur = 0, float(-inf)
            for i in range(row):
                for j in range(col):
                    if matrix[i][j]<=mid:
                        count+=1
                        if matrix[i][j]>cur:
                            cur = matrix[i][j]
            if count==k:
                return cur               
            if count>k:
                right = mid-1
            else:
                left = mid+1
        return left #***********如果不写这句 配合while left<=right 当要找的数字存在重复值，导致统计完的count>k了，就没法找到这个数字了，right=这个数字-1
        #如果改成right=mid，又会导致超时 哎

执行用时：360 ms, 在所有 Python3 提交中击败了8.71%的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了37.29%的用户
