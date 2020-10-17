class Solution:
    def myPow(self, x: float, n: int) -> float:
        def double(x,n):
            if n==0:
                return 1.0
            y=double(x,n//2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        return double(x,n) if n>0 else double(1/x,-n)
                
        
'''执行用时：
44 ms, 在所有 Python3 提交中击败了50.75%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了38.89%的用户'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        result=1
        while(n):
            if n&1: #二进制当前最右端位为1
                result*=x
            x*=x#计算x x2 x4 x8...x^(2^(n-1)) 对应位为1就乘上当前的x某次方 为0不管
            n>>=1 #移除最右端
        return result
    
    
'''执行用时：
36 ms, 在所有 Python3 提交中击败了90.72%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了5.48%的用户'''
