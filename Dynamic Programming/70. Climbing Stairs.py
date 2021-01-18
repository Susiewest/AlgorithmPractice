#递归超时转DP
class Solution:
    def climbStairs(self, n: int) -> int:
        #if n == 1: return 1
        #if n == 2: return 2
        #return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n==1: return 1
        if n==2: return 2
        x=1
        y=2
        temp=0
        for i in range(3,n+1):
            temp=x+y
            x=y
            y=temp
        return temp

'''执行结果：
通过
执行用时：
40 ms, 在所有 Python3 提交中击败了64.71%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了20.59%的用户'''
