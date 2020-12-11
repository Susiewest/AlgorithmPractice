一开始写的是max(dp[i-j]*j, dp[i]),但是dp[i-j]保存的是分绳子存的最大长度，其实i-j也可以不分。但不分没有保存到dp中，所以改为
max((i-j)*j,dp[i-j]*j,dp[i])分别对应，从j处剪一下，剩下i-j不剪了/从j处剪一下，剩下的继续剪/用于多次比较的工具人

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2]=1
        if n<=2:
            return dp[n]
        for i in range(3,n+1):
        #j从1到i也可以，不影响选最大的
            for j in range(i):
                dp[i] = max((i-j)*j,dp[i-j]*j,dp[i])
        return dp[-1]

执行用时：48 ms, 在所有 Python3 提交中击败了33.63%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了33.24%的用户
