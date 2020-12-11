题目类似于一个正整数可以拆成其他正整数的和,求这些正整数的最大连乘积。
将绳子 以相等的长度等分为多段 ，得到的乘积最大。
y=x^[(1/x)*n],n是常数，对y=x^(1/x)求导得知2.7几时有极大值。
x取整数3.
x对3取余得到b。对3整除得到a。
当b=0 时，直接返回 3^a,
当b=1 时，要将一个1+3 转换为2+2,因此返回 3^(a−1)×4,
当b=2 时，返回3^a×2。

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            return n-1
        a = n//3
        b = n%3
        if b==0:
            return int(math.pow(3,a))
        elif b==1:
            return int(math.pow(3,a-1)*4)
        else:
            return int(math.pow(3,a)*2)
执行用时：44 ms, 在所有 Python3 提交中击败了54.23%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.22%的用户

