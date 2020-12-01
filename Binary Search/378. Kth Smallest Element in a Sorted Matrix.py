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
     改成下面这样也行
     '''  while left<right:
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
                right = mid
            else:
                left = mid+1
        return left'''

执行用时：360 ms, 在所有 Python3 提交中击败了8.71%的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了37.29%的用户

这个矩阵的每一行均为一个有序数组。问题即转化为从这 n 个有序数组中找第 k 大的数，可以想到利用归并排序的做法，归并到第 k 个数即可停止。
一般归并排序是两个数组归并，而本题是 n 个数组归并，所以需要用小根堆维护，以优化时间复杂度。
n路归并 每次只需要把最新pop出来的那行 push新的进来
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k-1):  #为何要-1 因为第一个最小值已经排好的 不需要做操作
            num,x,y = heapq.heappop(pq)
            if y<n-1:
                heapq.heappush(pq,(matrix[x][y+1],x,y+1))
        return heapq.heappop(pq)[0]
执行用时：268 ms, 在所有 Python3 提交中击败了24.18%的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了18.68%的用户
