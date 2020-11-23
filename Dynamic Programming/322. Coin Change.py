class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp = [0 for i in range(amount+1)]
        dp = [amount+1 for i in range(amount+1)] #因为要找最小值min，初始化要设一个大一点的数
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
            #i-coin>=0 而非>0，coins中的面额去换硬币的时候，最小应该是1，写>0会导致 不能取到1
                if i-coin>=0:
                    #别忘了还要跟自己比
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[-1] if dp[-1]!=amount+1 else -1


执行用时：1360 ms, 在所有 Python3 提交中击败了77.44%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了30.15%的用户
