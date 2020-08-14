class Solution:
    def titleToNumber(self, s: str) -> int:
        exponent=0
        col=0
        for i in range(len(s)-1,-1,-1):
            col+=(ord(s[i])-ord('A')+1)*(26**exponent)
            exponent+=1
        return col



'''执行用时：
40 ms, 在所有 Python3 提交中击败了84.64%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了25.36%的用户'''
