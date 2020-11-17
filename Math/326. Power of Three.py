class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(n>1):
            n = n/3
        return n==1

执行用时：116 ms, 在所有 Python3 提交中击败了20.50%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了9.90%的用户

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        res = math.log10(n)/math.log10(3)
        return res-int(res)==0
执行用时：92 ms, 在所有 Python3 提交中击败了71.68%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了7.07%的用户
