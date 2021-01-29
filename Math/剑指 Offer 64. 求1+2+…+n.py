逻辑符短路,n = 1时停止
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
执行用时：64 ms, 在所有 Python3 提交中击败了15.18%的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了25.44%的用户

