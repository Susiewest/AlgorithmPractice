#md真是惊天大疑惑 计算第n项为啥不是计算f(n-1)
class Solution:
    def fib(self, n: int) -> int:
        # dp = [0 for _ in range(n)]
        # dp[0] = 0
        # dp[1] = 1
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a%1000000007
        
执行用时：28 ms, 在所有 Python3 提交中击败了99.00%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了24.96%的用户

from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return (self.fib(n-1)+self.fib(n-2))%1000000007

执行用时：48 ms, 在所有 Python3 提交中击败了15.55%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.11%的用户

