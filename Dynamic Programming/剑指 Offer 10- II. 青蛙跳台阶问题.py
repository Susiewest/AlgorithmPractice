from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numWays(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        return (self.numWays(n-1)+self.numWays(n-2))%1000000007
 
执行用时：48 ms, 在所有 Python3 提交中击败了15.73%的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了5.17%的用户

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a%1000000007

执行用时：36 ms, 在所有 Python3 提交中击败了84.77%的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了75.60%的用户
