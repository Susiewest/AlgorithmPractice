学习了一个库函数 replace(' ', '20%')
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

执行用时：32 ms, 在所有 Python3 提交中击败了94.24%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了6.79%的用户
