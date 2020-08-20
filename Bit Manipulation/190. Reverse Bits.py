class Solution:
    def reverseBits(self, n: int) -> int:
        new, trans=0, 31
        while(n):
            #一串数字n与000000000000001相与就是取最后一位数字
            last=n&1
            #左移31-i位 i从0开始
            new+=last<<trans
            trans-=1
            n=n>>1
        return new


'''执行用时：
44 ms, 在所有 Python3 提交中击败了59.95%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了53.77%的用户'''
