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
