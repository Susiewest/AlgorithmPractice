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
                
