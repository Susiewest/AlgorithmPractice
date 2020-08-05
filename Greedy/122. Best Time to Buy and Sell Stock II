#这个题看了题解写的 我直呼牛批 太厉害了这思路 谁看谁说吊
#遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit



'''执行结果：
通过
执行用时：
64 ms, 在所有 Python3 提交中击败了99.54%的用户
内存消耗：
15 MB, 在所有 Python3 提交中击败了32.68%的用户'''
