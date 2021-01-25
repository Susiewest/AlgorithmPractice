和121题一样
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0]*len(prices)
        min_price = prices[0]
        for i in range(1,len(prices)):
            dp[i] = max(dp[i-1],prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return max(dp)

执行用时：36 ms, 在所有 Python3 提交中击败了96.50%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了10.96%的用户
