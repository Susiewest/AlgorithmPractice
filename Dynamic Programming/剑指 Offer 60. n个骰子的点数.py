F（N,S）表示投第N个骰子时，点数和为S的次数
F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
首先初始化dp[1][]=1
然后需要注意的点是，s的取值起始位置不是固定为1，而是根据骰子个数变化的
最后保存结果的时候，n个骰子也不可能投出来和为1，2，3，...,n-1的

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0 for i in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    dp[i][j] += dp[i-1][j-k]
        result = []
        for i in range(n,6*n+1):
            result.append(dp[n][i]/6**n)
        return result
执行用时：44 ms, 在所有 Python3 提交中击败了40.54%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了20.18%的用户


