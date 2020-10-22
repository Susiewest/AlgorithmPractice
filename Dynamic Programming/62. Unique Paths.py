class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
'''执行用时：
36 ms, 在所有 Python3 提交中击败了90.50%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了5.04%的用户'''


#动态规划优化 只保存当前行和上一行
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        pre=[1]*n
        cur=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j]=cur[j-1]+pre[j]
                #dp[i][j]=dp[i-1][j]+dp[i][j-1]
            pre=cur
        return cur[-1]
        
'''执行用时：
28 ms, 在所有 Python3 提交中击败了99.48%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了5.21%的用户'''
