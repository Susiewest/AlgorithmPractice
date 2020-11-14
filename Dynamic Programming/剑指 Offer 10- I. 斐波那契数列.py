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

@functools.lru_cache(maxsize=None, typed=False)
使用 functools 模块的 lur_cache 装饰器，可以缓存最多 maxsize 个此函数的调用结果，从而提高程序执行的效率，特别适合于耗时的函数。参数 maxsize 为最多缓存的次数，如果为 None，则无限制，
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

