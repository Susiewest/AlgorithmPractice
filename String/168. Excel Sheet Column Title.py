#这个题 有点难 和26进制转换沾边
#对于能整除的数要单独处理
#对取余得到的数可以处理 从而在倒数的位置开始得到结果 所以递归写在return的最前面
#对于最后一次处理 如果说1-25 再次//26=0->''
#如果是26 26//26=1 col包含此次处理结果 此外还会多递归一次
class Solution:
    def convertToTitle(self, n: int) -> str:
        row=0
        col=0
        title=''
        if n==0: return ''
        #col 不是记录真正的列数 记录的是和第一列的差值/距离 
        if n%26!=0:
            col=n%26-1
            title=self.convertToTitle(n//26)+chr(ord('A')+col)
        else:
            col=(n-1)%26
            title=self.convertToTitle(n//26-1)+chr(ord('A')+col)
        return title


'''执行用时：
28 ms, 在所有 Python3 提交中击败了98.80%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了53.45%的用户'''
