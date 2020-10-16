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
