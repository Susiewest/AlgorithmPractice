#md好绝的做法 因为是z字形的 所以一会从下往上 一会从上往下 
#此时设置了一个step 每次换方向步长就取反 我tm直呼内行
#注意 一开始我让step=1 这样会把他首先变为-1又执行 就会越界 
#应该是设为-1开始 因为这也属于需要取反的情况
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:
            return s
        store_list=['' for _ in range(numRows)]
        row, step=0, -1
        for i in range(len(s)):
            store_list[row]+=s[i]
            if row==0 or row==numRows-1:
                step=-step
            row+=step
        return ''.join(store_list)

'''执行用时：
60 ms, 在所有 Python3 提交中击败了92.44%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了56.33%的用户'''
