#情况有限的条件下 能多列出就多列出 比如900 400 这种特殊情况 列出来会简化很多
#感觉自己写的还挺妙的 比答案还妙 略～
#题解说我这办法叫贪心法 我自己都不知道我这是贪心
class Solution:
    def intToRoman(self, num: int) -> str:
        #return一个字符串时 要么空字符串每次+ 要么空列表 每次append 最后join
        chart={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L',40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman=''
        for i in chart.keys():
            if num==0:
                return roman
            roman+=chart[i]*(num//i)
            num=num%i
        return roman
        

'''执行用时：
68 ms, 在所有 Python3 提交中击败了42.44%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了57.19%的用户'''
