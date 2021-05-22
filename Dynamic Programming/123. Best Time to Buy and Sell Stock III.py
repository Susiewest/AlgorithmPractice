做个人吧
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = prices[0]
        buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, -buy1 + prices[i])
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
执行用时：456 ms, 在所有 Python3 提交中击败了79.65%的用户
内存消耗：25.1 MB, 在所有 Python3 提交中击败了59.48%的用户

