python不能修改字符串，所以先反转前n，再反转后面，再整体反转的思路不可
这里取余的思路很赞

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        result = ''
        for i in range(n,n+len(s)):
            result+=s[(i%len(s))]
        return result
执行用时：40 ms, 在所有 Python3 提交中击败了64.09%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了20.54%的用户

