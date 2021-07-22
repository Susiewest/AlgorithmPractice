做个人吧 面试出hard
关键在于buy2的初始化，一开始初始化为0会导致错误
因为buy2其实不是我第二次要不要买，而是带上第一次我买了当前位置是多少钱，也许我现在买了是赔了，但我卖了就会赚
所以不要在buy2的时候初始化为0，因为这样取max基本上大概率就是会取到0然后不买。。不应该这样，而是要先赔钱才赚钱
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

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        for i in range(n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1+prices[i])
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, buy2+prices[i])
        return sell2
