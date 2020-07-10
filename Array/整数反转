class Solution:
    def reverse(self, x: int) -> int:
        #a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素，即倒序。
        y = abs(x);
        z = str(y);
        y = int(z[::-1])
        if x>=0 and -2**31<y<2**31-1:
            return y
        elif x<0 and -2**31<-y<2**31-1:
            return -y
        else:
            return 0
/*执行用时：
32 ms, 在所有 Python3 提交中击败了98.82%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了6.67%的用户*/
