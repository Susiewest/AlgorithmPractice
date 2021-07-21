#起初我想用双指针的办法 一个从前往后 一个从后往前 这样在list元素为奇数个的时候 中间的元素会被忽略掉
#以下是动态规划的办法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        min_buy=prices[0]      
        dp=[0]*len(prices)
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1],prices[i]-min_buy)
            min_buy=min(min_buy,prices[i])
        return dp[-1]
        
     
‘’‘执行结果：
通过
执行用时：
52 ms, 在所有 Python3 提交中击败了58.14%的用户
内存消耗：
14.4 MB, 在所有 Python3 提交中击败了96.43%的用户’‘’



#以下是我失败了的双指针

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=10000
        max_sell=0
        i=0
        j=len(prices)-1
        while(i<j):
            if prices[i]<min_buy:
                min_buy=prices[i]
            i+=1
            if prices[j]>max_sell:
                max_sell=prices[j]
            j-=1
        return max_sell-min_buy if max_sell-min_buy>0 else 0
即使单独处理了中间位置依然有错误
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=10000
        max_sell=0
        length=len(prices)
        i=0
        j=length-1
        while(i<j):
            if prices[i]<min_buy:
                min_buy=prices[i]
            i+=1
            if prices[j]>max_sell:
                max_sell=prices[j]
            j-=1
        if length%2==1 and prices[length//2]>max_sell:
            max_sell=prices[length//2]
        if length%2==1 and prices[length//2]<min_buy:
            min_buy=prices[length//2]
        return max_sell-min_buy if max_sell-min_buy>0 else 0
    
class Solution:
def maxProfit(self, prices: List[int]) -> int:
    # 因为只买卖一次，所以最大收益就是，每天卖的钱减去今天之前最低价（买入），所有结果里的最大值
    dp = [0]*len(prices)
    buy = -prices[0]
    for i in range(1, len(prices)):
        dp[i] = max(dp[i-1], prices[i]+buy)
        buy = max(buy, -prices[i])
    return dp[-1]
执行用时：268 ms, 在所有 Python3 提交中击败了58.85%的用户
内存消耗：22.8 MB, 在所有 Python3 提交中击败了89.38%的用户
