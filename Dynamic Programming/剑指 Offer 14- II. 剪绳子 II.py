class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],dp[i-j]*j,(i-j)*j)
        return dp[-1]%1000000007
执行用时：836 ms, 在所有 Python3 提交中击败了23.07%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.24%的用户

