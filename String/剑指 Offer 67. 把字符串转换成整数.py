和第8题相同，但第八题用了正则表达式+int()的API
其实不该用api，这里用新方法写一下
class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        result, flag = 0, 1
        max_num, min_num = 2**31-1, -2**31
        if str[0]=='-': flag = 0
        i = 0
        if str[i] in "+-": i+=1
        for c in str[i:]:
            if not '0'<=c<='9': break
            result = result*10 + ord(c)-ord('0')
        # 这里一开始写的>=，但是-2147483647，因为2147483647满足>=max_num，会return min_num，也就是-2147483648
        # 干脆把2147483647归类到return自己的范畴，而非return最大最小值的范畴，效果一样的
        if result>max_num:
            return max_num if flag else min_num
        else:
            return result if flag else -result
执行用时：40 ms, 在所有 Python3 提交中击败了81.55%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了8.99%的用户

