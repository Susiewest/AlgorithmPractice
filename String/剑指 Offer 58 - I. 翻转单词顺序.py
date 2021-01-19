class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        return ' '.join(temp[::-1])
执行用时：40 ms, 在所有 Python3 提交中击败了71.30%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了12.52%的用户

split()会把字符串中多个连续空格看作一个空格，split(' ')会一个空格就是一个空格
https://www.cnblogs.com/python-coder/p/10073329.html
